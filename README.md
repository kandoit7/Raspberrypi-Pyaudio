# Raspberrypi-Pyaudio

PyAudio - Raspberry PI - ( USB Audio Card {Input} || USB Mic )

Recording Audio.
Python

Writing the module code

channel = 1 (mono)
sampling rate = 48000 Hz
format = paInt16 -> 16bit ( signed int -32768 ~ 32767 )
chunk = 1024 (chunk is a buffer....? )
  exam..) pcmData <- [chunk = 1024] ====> pcmData[1024] = { x0, x1, x2, x3, ..... x1023 }
  
thread
