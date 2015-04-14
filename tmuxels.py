#!/usr/bin/python

import sys
import subprocess
import shlex

def get_terminal_size_tput():
    try:
        cols = int(subprocess.check_output(shlex.split('tput cols'))) 
        rows = int(subprocess.check_output(shlex.split('tput lines'))) - 1
        return (cols, rows)
    except:
        pass


def get_pane_size(hsplits, vsplits):
    w,h = get_terminal_size_tput()
    panex = (w - (int(hsplits)-1)) / int(hsplits)
    paney = (h - (int(vsplits)-1)) / int(vsplits)
    return (panex, paney)


def buildPS1(width, height):
    ps1=" " + "*" * (width-2) + " \n"
    for i in range(height-2):
        ps1+=" " + "*" * (width-2) + " \n"
    ps1+=" " + "*" * (width-2) 
    return ps1

#Create tmux session
def createTmux():
    subprocess.call(['tmux', '-2', 'new-session', '-d', '-n', '"tmuxtest"'])


#Horizontal splits
def splitHorizontal(hsplits):
    x, y = get_pane_size(sys.argv[1], sys.argv[2])
    #x = x/2
    for i in range(int(hsplits)-1): 
        subprocess.call(['tmux', 'split-window', '-d', '-h', '-l', str(x), '-t', '0'])

#Calculate Even Splits for Window size
def calc_even_splits():
    w,h = get_terminal_size_tput()
    for i in range(1,30):
        if ((w - (i - 1)) % i) == 0:
            print 'Try ' + str(i) + ' Hsplits.' 
        if ((h - (i - 1)) % i) == 0:
            print 'Try ' + str(i) + ' Vsplits.' 

#Vertical Splits
def splitVertical(vsplits):
    x, y = get_pane_size(sys.argv[1], sys.argv[2])
    for j in range(0, (int(sys.argv[1]) * int(sys.argv[2])) - 1, int(vsplits)):
        #print j 
        for k in range(int(vsplits) - 1):
            #print k
            if (j == 0):
                l = 0
            else:
                l = j + k
            
            subprocess.call(['tmux', 'split-window', '-v', '-l', str(y), '-t', str(l)])


def fillpanes():
    w,h = get_pane_size(sys.argv[1],sys.argv[2])
    ps1 = buildPS1(w,h)
    numpanes = int(int(sys.argv[1]) * int(sys.argv[2])) 
    for i in range(numpanes):
        print i
	subprocess.call(['tmux', 'select-pane','-t', str(i)])
        subprocess.call(['tmux', 'send-keys', '-t', str(i), 'export PS1="'+ps1+'"', 'Enter'])
        subprocess.call(['tmux', 'send-keys', '-t', str(i), 'clear', 'Enter']) 

if __name__ == "__main__":
    sizex, sizey = get_terminal_size_tput()
    print  'width =', sizex, 'height =', sizey
    #w,h = get_pane_size(sys.argv[1],sys.argv[2])
    #ps1 = buildPS1(w,h)
    #print ps1
    panex, paney = get_pane_size(sys.argv[1], sys.argv[2])
    print 'panex =',panex, 'paney =', paney
    createTmux()
    #calc_even_splits() 
    splitHorizontal(sys.argv[1])
    splitVertical(sys.argv[2])
    #subprocess.call(['./tmuxgraphics.sh', sys.argv[1], sys.argv[2]])
    fillpanes() 
