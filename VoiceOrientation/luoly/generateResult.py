import sys
import os
import threading

filename = sys.argv[1]

def exec_cmd(cmd):
    p = os.popen(cmd)
    x = p.read()
    print x
    p.close()

cmds = []
for i in range(0,4,):
    if i == 2 :
        continue
    cmd = "python readwav.py " + filename + "2.wav " + filename + str(i) + ".wav " + filename + "2.TextGrid " +  filename + str( i) + ".TextGrid >> log"
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



