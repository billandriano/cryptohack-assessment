def gcd_final_step(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    else:
        return 0

def gcd(a,b):
    a=max(a,b)
    b=min(a,b)
  
    
    while gcd(a,b)==0:
        c=a
        a=b
        b=c%b

    return gcd(a,b)

#print(gcd(66528,52920))