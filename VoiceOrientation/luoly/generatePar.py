import sys
import os
filename = sys.argv[1]
cmds = []
for i in range(1,5):
    cmd = "./maus SIGNAL=" + filename + str(i) + ".wav BPF=youtellme.par OUTFORMAT=TextGrid LANGUAGE=eng-US" 
    print cmd
    cmds.append(cmd)
for cmd in cmds:
    p = os.popen(cmd)
    x = p.read()
    print x
    p.close()
