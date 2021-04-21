from PyQt5 import QtCore
from threading import Thread, Event
import subprocess, time, core

def event(self):
    Thread.stop()

#def thread_finished(self):
    

Thread = core.EnumerationThread()
Thread.completion_signalconnect(event)
Thread.start()
#print(condition)