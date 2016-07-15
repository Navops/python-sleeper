import time
import random
import os

start = 30
stop = 60

if os.environ.has_key("SLEEP_START"):
    start = int(os.environ["SLEEP_START"])

if os.environ.has_key("SLEEP_STOP"):
    stop = int(os.environ["SLEEP_STOP"])

i = random.randint(start,stop)
print "Sleeping: %s seconds" % i
time.sleep(i)
