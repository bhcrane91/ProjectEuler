cipher = [int(i) for i in open("cipher.txt").read().split(",")]
print(cipher)

print(min(cipher),max(cipher))

def decrypt(n):
    return "".join(chr(c^n) for c in cipher)

for i in range(90,100):
    print()
    print(i)
    print(decrypt(i))
