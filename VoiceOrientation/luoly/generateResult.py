import sys
import os

filename = sys.argv[1]
cmds = []
for i in range(1,5,):
    if i == 2 :
        continue
    cmd = "python readwav.py " + filename + "2.wav " + filename + str(i) + ".wav " + filename + "2.TextGrid " +  filename + str( i) + ".TextGrid >> log"    
    print cmd
    cmds.append(cmd)

for cmd in cmds:
    p = os.popen(cmd)
    x = p.read()
    print x
    p.close()
