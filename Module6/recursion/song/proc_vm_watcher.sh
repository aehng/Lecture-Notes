#!/bin/sh

# This program needs the tput(1) program from ncurses
#   https://invisible-island.net/ncurses/
#
# And the watch(1) program from procps-ng
#   http://sourceforge.net/projects/procps-ng/

tput civis  # hide the cursor

if [ $# -gt 0 -a -f /proc/$1/status ]; then
    watch -d -e -n 0.5 grep -E '"Vm|Name"' /proc/$1/status
else
    echo "Usage: $0 PID"
fi
