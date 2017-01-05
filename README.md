# Raspberrypi-Pyaudio

PyAudio - Raspberry PI - ( USB Audio Card {Input} || USB Mic ) <br />

Recording Audio. <br />
Python <br />

Writing the module code <br />

1.channel = 1 (mono) <br />
2.sampling rate = 48000 Hz <br />
3.format = paInt16 -> 16bit ( signed int -32768 ~ 32767 ) <br />
4.chunk = 1024 (chunk is a buffer....? ) <br />
<t /> exam..) pcmData <- [chunk = 1024] ====> pcmData[1024] = { x0, x1, x2, x3, ..... x1023 } <br />
5.thread <br />
