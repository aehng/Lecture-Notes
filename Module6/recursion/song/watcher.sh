#!/bin/sh

# This program needs the tput(1) program from ncurses
#   https://invisible-island.net/ncurses/
#
# as well as the name of a terminal emulator that supports the `-e` option

# Change this to your favorite terminal if you don't have xterm(1) installed
TERMINAL=xterm

# one or two arguments ar required
if [ $# -eq 0 ]; then
    echo "Usage: $0 PROGRAM_NAME [iteratively]"
    exit 1
fi


# start up the program in the background & note its PID
case $1 in
    *.class)
        java ${1%.class} $2 &
        ;;
    *)
        if ! [ -x $1 ]; then
            echo $1 is not an executable program
            echo "Usage: $0 PROGRAM_NAME"
            exit 1
        else
            ./$1 $2 &
        fi
        ;;
esac
PID=$!

bold=`tput smso` offbold=`tput rmso`
echo "${bold}Press ENTER in this window to stop the child program${offbold}"

# spawn a new terminal, running the watcher script with the background PID
$TERMINAL -e "sh proc_vm_watcher.sh $PID" 2>/dev/null &

read WAIT_FOR_IT
kill $PID
