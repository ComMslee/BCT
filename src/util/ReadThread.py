import copy
import time

from PySide6 import QtCore
from PySide6.QtCore import QThread, QMutexLocker, QMutex


class ReadThread(QThread):
    msgAck = QtCore.Signal(bytes)
    msgReadSerial = QtCore.Signal(str)
    msgReadRealTime = QtCore.Signal(list)

    def __init__(self, serial_port):
        super().__init__()
        self.serial_port = serial_port
        self.mutex = QMutex()
        self.bRunning = True

    def run(self):
        with QMutexLocker(self.mutex):
            try:
                if self.serial_port.isOpen():
                    buffer: bytes = None
                    while self.bRunning:
                        bytes_waiting = self.serial_port.in_waiting
                        if bytes_waiting > 0:
                            readData: bytes = self.serial_port.read(bytes_waiting)  # 수신 대기 중인 모든 데이터를 읽음

                            if buffer is not None:
                                readData = buffer + readData
                                buffer = None
                                print(f"is buffer --> Join {self.hexText(readData)}")

                                index = readData.find(b'\xA5')
                                if index > 0:
                                    readData = readData[index:]
                                    print(f"cut index {index} | {self.hexText(readData)}")

                            while len(readData) > 1 and readData[0] == 0xA5:
                                total_len = readData[1] + 4
                                if total_len > len(readData):
                                    buffer = copy.deepcopy(readData)
                                    print(
                                        f"Packet Under [needTo {str(total_len)}|current {str(len(readData))}][{self.hexText(readData)}]")
                                    break
                                elif total_len < len(readData):
                                    buffer = readData[total_len:]
                                    readData = readData[:total_len]
                                    print(
                                        f"Packet Over [needTo {str(total_len)}][ {self.hexText(readData)} | {self.hexText(buffer)} ]")

                                # in data
                                rt = self.parser(readData)
                                if rt:
                                    if buffer is None:
                                        break
                                    else:
                                        readData = buffer
                                        buffer = None
                                else:
                                    print("self.parser false..")

                            if not (len(readData) > 1 and readData[0] == 0xA5):
                                print(f"Packet Not {self.hexText(readData)}")
                                buffer = copy.deepcopy(readData)

                        time.sleep(0.1)  # 작업을 반복하기 전에 잠시 대기

            except Exception as error:
                print(error)

    def parser(self, parserData: bytes) -> bool:
        data_len = len(parserData)
        if data_len > 1 and parserData[0] == 0xA5:
            total_len = parserData[1] + 4
            lastPacket = parserData[data_len - 1]
            if total_len == data_len and lastPacket == 0x7E:
                if parserData[2] == 0x81:
                    print(f"STS_ACK [err {parserData[3]}][rev {parserData[4]}]")
                    self.msgAck.emit(bytes([parserData[3], parserData[4]]))
                elif parserData[2] == 0x82:
                    current = self.decodeWord(parserData[9], parserData[10], 0.02, True)
                    voltage = self.decodeWord(parserData[11], parserData[12], 0.002)
                    tempAvg = parserData[19]
                    progrssbar = parserData[23]
                    info_string = (
                        f"STS_INFO "
                        f"BmsMode {parserData[3]} | "
                        f"PwrCFET {parserData[4]}, DFET {parserData[5]} | "
                        f"DiagInfo {parserData[6]} | "
                        f"IgnitionRecog {parserData[7]} | "
                        f"FullyCharged {parserData[8]} | "
                        f"Current {current} / {self.decodeWord(parserData[15], parserData[16], 0.02, True)} | "
                        f"Voltage {voltage} / {self.decodeWord(parserData[17], parserData[18], 0.002)} | "
                        f"estRSOC {parserData[13]}, SOH {parserData[14]} | "
                        f"TempCell Avg {tempAvg}, Max {parserData[20]}, Min {parserData[21]} | "
                        f"ChargeMode {parserData[22]} | "
                        f"ProgressBarState {progrssbar}"
                    )
                    print(info_string)

                    data_82 = [current, voltage, tempAvg, progrssbar]

                    self.msgReadRealTime.emit(data_82)

                elif parserData[2] == 0x83:
                    text = ''.join(chr(byte) for byte in parserData[4:19])
                    print(f"STS_SERIAL_NUMBER [{parserData[3]}] {text}")
                    self.msgReadSerial.emit(text.replace('\x00', ''))

                else:
                    print(f"parser not Know command {self.hexText(parserData)}")

                return True
            else:
                print(f"parser not my packet {total_len} | {data_len} | {self.hexText(bytes([lastPacket]))}")
                return False
        else:
            print(f"parser not my packet {data_len} {parserData[0]}")
            return False

    def hexText(self, data: bytes) -> str:
        return ' '.join(format(byte, '02X') for byte in data)

    def decodeWord(self, low_byte, high_byte, resolation: float = 1.0, signed: bool = False):
        word_value = int.from_bytes(bytes([high_byte, low_byte]), byteorder='big', signed=signed)
        if resolation != 1.0:
            result = int(value * resolation * 100) / 100  # 소수점 이하 2자리까지 버림
        else:
            result = value
        return result

    def decodeByte(self, byte, resolation: float = 1.0, signed: bool = False):
        value = int.from_bytes(bytes([byte]), byteorder='big', signed=signed)
        if resolation != 1.0:
            result = int(value * resolation * 100) / 100  # 소수점 이하 2자리까지 버림
        else :
            result = value
        return result

    def encodeSignedWord(self, word_value) -> bytes:
        if word_value < -32768 or word_value > 32767:
            raise ValueError("Value out of range for signed short: " + str(word_value))
        return word_value.to_bytes(2, byteorder='big', signed=True)
    def encodeSignedByte(self, value) -> bytes:
        if value < -128 or value > 127:
            raise ValueError("Value out of range for signed byte: " + str(value))
        return value.to_bytes(1, byteorder='big', signed=True)

    def stop(self):
        self.bRunning = False
