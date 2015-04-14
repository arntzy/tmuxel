#!/bin/bash

#TODO LIST
#Figure out how to divide evenly into the screen given dividing lines
#Check for maximum number of windows
#Supply usage documentation

tmux -2 new-session -d -n 'tmuxtest'

#Determine Terminal Window Size
let lines=$(tput lines)
let columns=$(tput cols)
echo "Lines: " $lines
echo "Columns: " $columns

#Global Variables for the Splits
let hsplits=$1
let vsplits=$2
let vchar=lines/vsplits
let hchar=columns/hsplits
let limit=(hsplits-1)*vsplits
echo "hchar: $hchar"
echo "vchar: $vchar"
echo "limit: $limit"

#Horizontal splits
for((i=0;i<hsplits-1;i++))
	do
	#echo $i 
	#tmux select-pane -t $i
	tmux split-window -d -h -l $hchar -t 0
	#echo tmux split-window -h -l $hchar -t 0 
	done

#Probably not necessary
#tmux select-layout even-horizontal

#Vertical Splits
for((j=0;j<=limit;j+=vsplits))
	do
	#echo $j
	for((k=0;k<vsplits-1;k++))
		do
		#echo $k
		if [ $j -eq 0 ]; then
		let l=0
		else
		let l=j+k
		fi
		#echo l=$l
		#tmux select-pane -t $j
		#echo tmux select-pane -t $j
		tmux split-window -v -l $vchar -t $l 
		#echo tmux split-window -v -l $vchar -t $l 
		done
		#tmux select-layout even-vertical
	done

#Build Export Strings
#buildPS1(){
	#let h=$1
	#let v=$2
	##let ps1="*"
	#echo $(printf '*%.0s' {1..$h})
#}

#buildPS1 $hchar $vchar

#let ps1=$(buildPS1 hchar vchar)
#echo $ps1

#Cycle through panes and export new prompt
#let panes=hsplits*vsplits

#for ((i=0;i<$panes;i++))
	#do
	##tmux display-message -pt 0 -F '#{pane_width}x#{pane_height}'
	#tmux select-pane -t $i		
	##export PS1="\033[01;32m\]\$"
	##tmux -c "export PS1='***'"
	#tmux send-keys -t $i 'export PS1="****"' Enter
	#tmux send-keys -t $i 'clear' Enter
	#done

#Attach the session
#tmux attach-session 
