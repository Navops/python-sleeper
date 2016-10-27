import time
import random
import os
import signal
import sys

start = 30
stop = 60

def handler(signum, frame):
    print "Exiting on signal", signum
    sys.exit(128+signum)

signal.signal(signal.SIGTERM, handler)

if os.environ.has_key("SLEEP_START"):
    start = int(os.environ["SLEEP_START"])

if os.environ.has_key("SLEEP_STOP"):
    stop = int(os.environ["SLEEP_STOP"])

i = random.randint(start,stop)
print "Sleeping: %s seconds" % i
time.sleep(i)
sys.exit(0)
