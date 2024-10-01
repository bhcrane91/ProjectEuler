#!/bin/zsh

d="$1"

cd problems
mkdir "$d"
cd "$d"
touch J${d}.java
cp ../../solutions/${d}.py P${d}.py 
touch NP${d}.py
touch R${d}.rs
touch L${d}.jl
echo "class J${d} {\n\tpublic static void main(String[] args) {\n\n\t}\n}" >> J${d}.java
touch README.md