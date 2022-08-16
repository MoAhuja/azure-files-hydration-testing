#!/bin/sh
max=$1
for (( i=1; i <= $max; i++ ))
do
    mkdir $2$i
    cp test.html $2$i
done