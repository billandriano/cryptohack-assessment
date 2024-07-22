from matrix2bytes import *

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    i=0
    j=0
    addroundkeymatrix=[[0 for col in range(4)] for row in range(4)]
    for i in range(0,len(s)):
        for j in range(0,len(s)):
            addroundkeymatrix[i][j]=s[i][j]^k[i][j]
    return addroundkeymatrix



#print(matrix2bytes(add_round_key(state, round_key)))
