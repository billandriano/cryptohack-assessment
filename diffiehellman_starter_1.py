g = 209
p = 991
fc = 1

x=1
while x!=p and (g * x) % p != fc:
    x+=1
if (g * x) % p == fc:
    print(x)
   