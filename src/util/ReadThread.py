import copy
import time

from PySide6 import QtCore
from PySide6.QtCore import QThread, QMutexLocker, QMutex


class ReadThread(QThread):
    msgRead = QtCore.Signal(str)
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

                elif parserData[2] == 0x82:
                    info_string = (
                        f"STS_INFO BmsMode {parserData[3]} | "
                        f"stsPwrCFET {parserData[4]} | "
                        f"stsPwrDFET {parserData[5]} | "
                        f"stsDiagInfo {parserData[6]} | "
                        f"stsIgnitionRecog {parserData[7]} | "
                        f"stsFullyCharged {parserData[8]} | "
                        f"word msrCurrentPack {self.makeWord(parserData[9], parserData[10])} | "
                        f"word msrVoltagePack {self.makeWord(parserData[11], parserData[12])} | "
                        f"estRSOC {parserData[13]} | "
                        f"estSOH {parserData[14]} | "
                        f"word ctrlChargerLimitCurrent {self.makeWord(parserData[15], parserData[16])} | "
                        f"word ctrlChargerLimitVoltage {self.makeWord(parserData[17], parserData[18])} | "
                        f"bms0_msrTempCellAvg {parserData[19]} | "
                        f"bms0_msrTempCellMax {parserData[20]} | "
                        f"bms0_msrTempCellMin {parserData[21]} | "
                        f"ChargeMode {parserData[22]} | "
                        f"ProgressBarState {parserData[23]}"
                    )
                    print(info_string)

                    data_82 = [self.makeWord(parserData[9], parserData[10]),
                               self.makeWord(parserData[11], parserData[12]), parserData[19]]

                    self.msgReadRealTime.emit(data_82)

                elif parserData[2] == 0x83:
                    text = ''.join(chr(byte) for byte in parserData[4:19])
                    print(f"STS_SERIAL_NUMBER [{chr(parserData[3])}] {text}")
                    self.msgRead.emit(text)

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

    def makeWord(self, low_byte, high_byte):
        word = (high_byte << 8) | low_byte
        return word

    def stop(self):
        self.bRunning = False
