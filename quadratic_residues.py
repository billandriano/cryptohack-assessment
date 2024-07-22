from euclidean_algorithm import *

def is_perfect_square(n):  
    i = 1  
    while i * i <= n:  
        if i * i == n:  
            return True  
        i += 1  
    return False

def quad_res(a,p):
    pos_a= [i for i in range(1,p) if gcd(p,i)==1]
    return_list=[]
    for b in pos_a:
        if is_perfect_square(p*b+a)==True:
             return_list.append(p*b+a)
    return return_list

def main():
    square_root=[]
    p = 29
    ints = [14, 6, 11]
    for i in ints:
       if quad_res(i,p) != []:
        for j in quad_res(i,p):
            square_root.append(j**0.5)
    return square_root


for i in main():
    print(i)
