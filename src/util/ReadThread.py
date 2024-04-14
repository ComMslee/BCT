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
                            data: bytes = self.serial_port.read(bytes_waiting)  # 수신 대기 중인 모든 데이터를 읽음
                            hex_data = ' '.join(format(byte, '02X') for byte in data)

                            data_len = len(data)
                            if data_len and data[0] == 0xA5:
                                total_len = data[1] + 4
                                if total_len != data_len:
                                    print("not match " + str(total_len) + " / " + str(data_len))

                                if data[2] == 0x81:
                                    print("STS_ACK [err " + str(data[3]) + "][rev " + str(data[4]) + "]")
                                elif data[2] == 0x82:
                                    print("STS_INFO"+
                                          "")
                                elif data[2] == 0x83:
                                    print("STS_SERIAL_NUMBER")
                                else:
                                    print("else" + hex_data)
                            else:
                                print("Out Data : ", hex_data)
                                # buferr = copy.deepcopy(data)

                        time.sleep(0.1)  # 작업을 반복하기 전에 잠시 대기
            except Exception as error:
                print(error)

    def makeWord(self, low_byte, high_byte):
        word = (high_byte << 8) | low_byte
        print(word)
        return word

    def stop(self):
        self.bRunning = False
