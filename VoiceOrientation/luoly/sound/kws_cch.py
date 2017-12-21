"""
Record audio from a 6+1 mic array, and then search the keyword "snowboy".
After finding the keyword, Direction Of Arrival (DOA) is estimated.

The hardware is respeaker 6+1 usb mic array:
    https://www.seeedstudio.com/ReSpeaker-Mic-Array-Far-field-w--7-PDM-Microphones--p-2719.html
"""


import time
from voice_engine.source import Source
from voice_engine.channel_picker import ChannelPicker
from voice_engine.kws import KWS
#from voice_engine.doa_respeaker_6p1_mic_array import DOA
from voice_engine.doa_respeaker_4mic_array import DOA
from voice_engine.file_sink import FileSink 

def main():
    src = Source(rate=16000, channels=4)
    ch1 = ChannelPicker(channels=4, pick=1)
    kws = KWS()
    doa = DOA(rate=16000)
    src.link(ch1)
    ch1.link(kws)
    src.link(doa)
    outf = "./log/test.wav"
    fsall = FileSink(outf, rate=16000, channels=4)
    src.link(fsall)
    #ch1.link(fs)
    for i in range(4):
        ch = ChannelPicker(channels=4, pick=i)
        src.link(ch)
        outf = "./log/test"+str(i)+".wav"
        fs = FileSink(outf, rate=16000, channels=1)
        ch.link(fs)


    def on_detected(keyword):
         print('detected {} at direction {}'.format(keyword, doa.get_direction()))

    kws.set_callback(on_detected)

    src.recursive_start()
    i = 0
    while i != 3:
        try:
            time.sleep(1)
            i = i + 1
        except KeyboardInterrupt:
            break

    src.recursive_stop()


if __name__ == '__main__':
    main()
