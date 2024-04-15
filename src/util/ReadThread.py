import copy
import time

from PySide6.QtCore import QThread, QMutexLocker, QMutex


class ReadThread(QThread):
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
                    print("STS_ACK [err " + str(parserData[3]) + "][rev " + str(parserData[4]) + "]")
                elif parserData[2] == 0x82:
                    print("STS_INFO" +
                          " BmsMode " + str(parserData[3]) +
                          " | stsPwrCFET " + str(parserData[4]) +
                          " | stsPwrDFET " + str(parserData[5]) +
                          " | stsDiagInfo " + str(parserData[6]) +
                          " | stsIgnitionRecog " + str(parserData[7]) +
                          " | stsFullyCharged " + str(parserData[8]) +
                          " | word msrCurrentPack "
                          + str(self.makeWord(parserData[9], parserData[10])) +
                          " | word msrVoltagePack "
                          + str(self.makeWord(parserData[11], parserData[12])) +
                          " | estRSOC " + str(parserData[13]) +
                          " | estSOH " + str(parserData[14]) +
                          " | word ctrlChargerLimitCurrent "
                          + str(self.makeWord(parserData[15], parserData[16])) +
                          " | word ctrlChargerLimitVoltage "
                          + str(self.makeWord(parserData[17], parserData[18])) +
                          " | bms0_msrTempCellAvg " + str(parserData[19]) +
                          " | bms0_msrTempCellMax " + str(parserData[20]) +
                          " | bms0_msrTempCellMin " + str(parserData[21]) +
                          " | ChargeMode " + str(parserData[22]) +
                          " | ProgressBarState " + str(parserData[23])
                          )
                elif parserData[2] == 0x83:
                    print("STS_SERIAL_NUMBER" +
                          "[" + chr(parserData[3]) + "]" +
                          chr(parserData[4]) +
                          chr(parserData[5]) +
                          chr(parserData[6]) +
                          chr(parserData[7]) +
                          chr(parserData[8]) +
                          chr(parserData[9]) +
                          chr(parserData[10]) +
                          chr(parserData[11]) +
                          chr(parserData[12]) +
                          chr(parserData[13]) +
                          chr(parserData[14]) +
                          chr(parserData[15]) +
                          chr(parserData[16]) +
                          chr(parserData[17]) +
                          chr(parserData[18])
                          )
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
