#!/usr/bin/env python3
with open("c.in", 'r') as f:
    lines = f.readlines()
lines.pop(0)
tbits = 0
dataset = 0
for line in lines:
    line = line.split()
    if line[0] == "**********":
        dataset += 1
        print("Data Set " + str(dataset) + ": $" + format(float(tbits)/1000, "0.2f"))
        tbits = 0
        continue
    for word in line:
        for c in word:
            c = ord(c)
            for i in range(8):
                tbits += c & 1
                c >>= 1
