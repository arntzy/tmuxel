#!/bin/bash

tmux -2 new-session -d -n 'tmuxtest'
panes=(0 1)

#Horizontal splits
for i in {0..20}; 
	do
	   tmux split-window -h -t $i 
	   tmux select-layout even-horizontal
        done

#tmux select-pane -t 0


#for h in "${panes[@]}"
#	do	
#		echo $h
#	done
#tmux split-window -v -l 4 -d -t 0


#for k in "${panes[@]}"
for k in {0..21};
	do
	   for j in {0..12}; 
		   do
		       #tmux select-pane -t $k 
		       tmux split-window -v -l 3 -t $k 
		       #tmux select-layout even-vertical
		   done
	done

tmux attach-session 


#This is a test of my keylogging skills




#split-window [-bdhvP] [-c start-directory] [-l size | -p percentage] [-t target-pane] [shell-command] [-F format] This is a test of a keystroke logger
