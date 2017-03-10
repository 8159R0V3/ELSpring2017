#!/usr/bin/python
from time import localtime, strftime
xdate = strftime("%Y-%m-%d", localtime())
xtime = strftime("%H-%M-%S", localtime())
Time = [xdate, xtime];
fo = open("testTime.db", "rw+")
print "testTime: ", fo.name
fo.seek(0, 2)
line = fo.write( xdate + " " + xtime+ "\n")
fo.close()
