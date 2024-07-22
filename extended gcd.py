def extended_gcd(a,b):
    if min(a,b)==0:
        return (max(a,b),0,1)
    else:
        (gcd, u, v) = extended_gcd(b % a, a)
        return (gcd, v - (b // a) * u, u)

p = 26513
q = 32321

print(extended_gcd(26513, 32321))