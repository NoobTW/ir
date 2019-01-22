#!/bin/bash

ret=`python -c 'import sys; print("%i" % (sys.hexversion<0x03000000))'`
if [ $ret -eq 0 ]; then
    echo "You have to install python 2 to keep using this script."
	exit
fi

echo Generating weight1.txt......
python mid_1.py > weight1.txt

echo Generating weight2.txt......
python mid_2.py > weight2.txt

echo Done.
