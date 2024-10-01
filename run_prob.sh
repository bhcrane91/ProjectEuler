#!/usr/bin/env zsh

n="$1"

cd problems/${n}/
javac J${n}.java 
rustc R${n}.rs
echo "\n----- Times -----\n"

javaT=$(time java J${n})
rustT=$(time ./R${n})
pythT=$(time python3.11 P${n}.py)
numpT=$(time python3.11 NP${n}.py)
juliT=$(time julia L${n}.jl)

echo ""
echo "$javaT"
echo "$rustT"
echo "$pythT"
echo "$numpT"
echo "$juliT"
