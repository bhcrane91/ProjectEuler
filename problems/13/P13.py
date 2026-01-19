with open("digits.txt","r") as f:
    numbers = sum([int(number[:10]) for number in f.read().split("\n")])

print(numbers)