import math as m

n = "1_2_3_4_5_6_7_8_9_0"
a = n.replace("_","")
l = int(m.sqrt(float(n.replace("_","0"))))
k = int(m.sqrt(float(n.replace("_","9"))))
print(l,k)
print(len(n))
print(m.log10(l),m.log10(k))

for i in range(l,k,10):
    if str(i**2)[::2] == a:
        print(i)


