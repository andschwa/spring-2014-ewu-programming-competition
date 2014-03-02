#!/usr/bin/env python3

with open("g.in", "r") as f:
        lines = f.readlines()
for perm in lines:
    result = True
    perm = perm.split()
    if len(perm) == 1 and int(perm[0]) == 0:
        break
    perm.pop(0)
    perm = [int(i) for i in perm]
    for i in range(len(perm)):
        for j in range(i+1, len(perm)):
            value = perm[j]-perm[i]
            for k in range(j+1, len(perm)):
                if perm[k]-perm[j] == value:
                    result = False
                    break
    if result:
        print("yes")
    else:
        print("no")
