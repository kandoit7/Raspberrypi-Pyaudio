# Raspberrypi-Pyaudio

<snippet>
  <content><![CDATA[

PyAudio - Raspberry PI - ( USB Audio Card {Input} || USB Mic )

Recording Audio.
Python

Writing the module code

1.channel = 1 (mono)
2.sampling rate = 48000 Hz
3.format = paInt16 -> 16bit ( signed int -32768 ~ 32767 )
4.chunk = 1024 (chunk is a buffer....? )
  exam..) pcmData <- [chunk = 1024] ====> pcmData[1024] = { x0, x1, x2, x3, ..... x1023 }
5.thread

]]></content>
  <tabTrigger>readme</tabTrigger>
</snippet>
