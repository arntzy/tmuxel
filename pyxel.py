#!/usr/bin/python

import os
import sys
import subprocess
import shlex
import random

FNULL = open(os.devnull, 'w')

for i in range(2000):
#while 1:
	i = random.randrange(0, int(sys.argv[1]))
	c = subprocess.call(['tmux', 'select-pane','-t', str(i)])
	a = subprocess.call(['tmux', 'send-keys', '-t', str(i), 'export PS1="\e[0;31m\$"', 'Enter'], stdout=FNULL, stderr=subprocess.STDOUT)
	b = subprocess.call(['tmux', 'send-keys', '-t', str(i), 'clear', 'Enter'], stdout=FNULL, stderr=subprocess.STDOUT) 

FNULL.close()

#retcode = subprocess.call(['echo', 'foo'], stdout=FNULL, stderr=subprocess.STDOUT)

