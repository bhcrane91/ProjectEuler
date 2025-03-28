#!/bin/zsh

d="$1"

cd problems
mkdir "$d"
cd "$d"
touch J${d}.java
touch P${d}.py 
touch NP${d}.py
touch R${d}.rs
touch L${d}.jl
touch C${d}.c
echo -e "class J${d} {\n\tpublic static void main(String[] args) {\n\n\t}\n}" >> J${d}.java
echo -e "int main() {\n\n\treturn 0;\n}" >> C${d}.c
echo -e "fn main() {\n\n}" >> R${d}.rs
echo -e "function main()\n\nend" >> L${d}.jl
touch README.md