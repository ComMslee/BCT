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
                    while self.bRunning:
                        bytes_waiting = self.serial_port.in_waiting
                        if bytes_waiting > 0:
                            data : bytes= self.serial_port.read(bytes_waiting)  # 수신 대기 중인 모든 데이터를 읽음
                            hex_data = ' '.join(format(byte, '02X') for byte in data)

                            if len(data) > 2 and data[0] == 0xA5:
                                if data[2] == 0x81:
                                    print("STS_ACK")
                                elif data[2] == 0x82:
                                    print("STS_INFO")
                                elif data[2] == 0x83:
                                    print("STS_SERIAL_NUMBER")
                                else :
                                    print("else" + hex_data)
                            else:
                                print("Out Data : ", hex_data)

                        time.sleep(0.1)  # 작업을 반복하기 전에 잠시 대기
            except Exception as error:
                print(error)

    def stop(self):
        self.bRunning = False
