
import sys
import wave
import numpy as np
from gcc_phat import gcc_phat

print("start")
sig1 = wave.open("test2.wav", 'rb')#near
ref1 = wave.open("test3.wav", 'rb')#far
rate = sig1.getframerate()

N = rate
window = np.hanning(N)

while True:
    sig = sig1.readframes(N)
    if len(sig) != 2 * N:
        break
    ref = ref1.readframes(N)
    sig_buf = np.fromstring(sig, dtype='int16')
    ref_buf = np.fromstring(ref, dtype='int16')
    tau, _ = gcc_phat(sig_buf * window, ref_buf * window, fs=rate, max_tau=1)
    print(tau)

