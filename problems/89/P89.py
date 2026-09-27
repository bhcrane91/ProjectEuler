nums = open("roman.txt","r").read().split("\n")

roman_to_int = {
    "M":1000,
    "D":500,
    "C":100,
    "L":50,
    "X":10,
    "V":5,
    "I":1
}
int_to_roman = {v:k for k,v in roman_to_int.items()}

for roman in nums:



