import pyaudio
import threading
import numpy as np
import socket

class SPaudio():
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.CHUNK = 1024
        self.RATE = 48000
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.addr = ('127.0.0.1', 1234)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
    def receiveData(self):
        try:
            self.pcmData = np.fromstring(self.stream.read(self.CHUNK), dtype=np.int16)
        except Exception as E:
            print(E, "\n")
            self.KeepRecording = False
        if self.KeepRecording:
            self.thread_start()
        else:
            self.stream.close()
            self.p.terminate()

    def close(self):
        self.stream.stop_stream()
        self.p.terminate()

    def thread_start(self):
        self.th = threading.Thread(target=self.receiveData)
        self.th.start()

    def record_start(self):
        self.KeepRecording = True
        self.pcmData = None
        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  frames_per_buffer=self.CHUNK
                                  )
        self.thread_start()


if __name__ == "__main__":

    record = SPaudio()
    record.record_start()
    while True:
        print record.pcmData

    record.close()
