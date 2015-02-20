#!/bin/bash
TODO: UPDATE TMUX ON THIS DROPLET SO YOU CAN resize panes

tmux -2 new-session -d -n 'tmuxtest'
#tmux new-window -n 'windowtest'

for i in {0..5}; 
	do
	   tmux split-window -h -t $i 
        done

 tmux resize-pane -t 0 -x 2
#tmux split-window -h
#tmux select-pane 
tmux select-pane -t 0
tmux attach-session 




#split-window [-bdhvP] [-c start-directory] [-l size | -p percentage] [-t target-pane] [shell-command] [-F format]
