#!/bin/bash

if [ $# -lt 1 ]
then
    echo "Usage : $0 <session name (IP)>"
    exit 1
fi

IP=$1
tmux new-session -s $IP \; \
setenv IP $IP \; \
send-keys "export IP=$IP" C-m \; \
split-window -v \; \
send-keys "tmux kill-pane -t 1" C-m \; \
send-keys "clear" C-m \;
