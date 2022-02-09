#!/bin/bash

#first the file
#second the interpretator of the file

echo %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
echo
echo "add the #!"$(which $2) for $1
echo
echo %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

tail -n+2 $1 > tmp 
echo "#\!"$(which $2) > $1
cat tmp >> $1
