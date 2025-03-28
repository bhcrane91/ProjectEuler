import numpy as np

hundreds = {
    100: 'onehundred',
    200: 'twohundred',
    300: 'threehundred',
    400: 'fourhundred',
    500: 'fivehundred',
    600: 'sixhundred',
    700: 'sevenhundred',
    800: 'eighthundred',
    900: 'ninehundred'
}

digits = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

teens = {
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}

tens = {
    0: '',
    10: 'ten',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

def parse_num(n):
    num = []
    i = 1
    while n > 0:
        last = n % (10**i)
        n -= last
        i += 1
        num.append(last)
    return num 

dicts = [digits,tens,hundreds]
letters = 0
for i in range(1,1000):
    numstr = ''
    teen = i % 100
    sub = 0
    if teen > 10 and teen < 20:
        numstr += teens[teen]
        sub = teen
    num = parse_num(i-sub)
    for idx, l in enumerate(num):
        if l >= 100 and teen > 0:
            numstr = 'and' + numstr
        numstr = dicts[idx][l] + numstr 
    letters += len(numstr)
    # print(i, numstr, len(numstr), letters)
    
    
letters += len('onethousand')
print(letters)
    

        
        
    
        