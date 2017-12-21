import sys
import os
import threading
filename = sys.argv[1]
cmds = []

def exec_cmd(cmd):
    p = os.popen(cmd)
    x = p.read()
    print x
    p.close()


for i in range(0,4):
    cmd = "./maus SIGNAL=" + filename + str(i) + ".wav BPF=youtellme.par OUTFORMAT=TextGrid LANGUAGE=eng-US"
    cmds.append(cmd)

# threads pool
threads = []

# create four threads
try:
    for cmd in cmds:
        th = threading.Thread(target=exec_cmd, args=(cmd,))
        print cmd
        th.start()
        threads.append(th)
except:
   print "Error: unable to start thread"

for th in threads:
    th.join()
