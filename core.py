from PyQt5 import QtCore
from threading import Thread, Event

class DomainThread(QtCore.QThread):
        connection = QtCore.pyqtSignal(list)

        def __init__(self):
            super(DomainThread, self).__init__()
        
        def print_subdomains(self):
            count = 0
            with open("Subdomains/subdomains1.txt","r") as f:
                content = f.readlines()
                if count <= 99:
                    count = count + 1
                    self.connection.emit(count)
                self.connection.emit(content)
            count=100
            self.connection.emit(count)
            self.stop()

        def stop(self):
            self._isRunning = False
            self.terminate()
            self.wait(100)