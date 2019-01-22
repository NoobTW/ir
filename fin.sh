#!/bin/bash

ret=`python -c 'import sys; print("%i" % (sys.hexversion<0x03000000))'`
if [ $ret -eq 0 ]; then
    echo "You have to install python 2 to keep using this script."
	exit
fi

python fin.py
