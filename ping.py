#! /usr/bin/python
#author PAING HEIN THU
#20160117
#sample ping status

import subprocess
import time
import sys

def Ping_result(address):
    try:
        while True:
            cmd = ['ping','-c', '1', address]
            res = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()
            if res == 0:
                print '.',
            else:
                print 'x',
            sys.stdout.flush()
            time.sleep(0.5)
    except:
        print "\n BYE BYE"

if __name__ == '__main__':
    Ping_result(sys.argv[1])
