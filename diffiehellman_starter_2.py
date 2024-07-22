p = 28151

number=1

for i in range(p):
    for n in range(p):
       if number%p==i^n:
        print(i)
       else:
         number+=1