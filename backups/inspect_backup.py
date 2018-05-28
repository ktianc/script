#!/usr/bin/python
#coding=utf-8

import os
import sys
import time


pid = os.popen("pgrep python").read()

if "22060" in pid:
	print "GETLOADAVG OK : Normal service."
    sys.exit(0)
else:
	print "GETLOADAVG CRITICAL : Can't find PID."
	sys.exit(2)