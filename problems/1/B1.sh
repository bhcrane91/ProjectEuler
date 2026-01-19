#!/bin/bash
x=0
a=1000
for i in $(seq 1 $a); do ((i%3==0 || i%5==0)) && x=$((x+i)); done
echo "Sum of multiples of 3 or 5 below $a: $x";
