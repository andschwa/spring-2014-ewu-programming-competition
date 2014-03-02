# Team 32
lines = []
with open("i.in", 'r') as File:
    lines = File.readlines()
lines.pop(0)
for line in lines:
    coords = line.split()
    x, y = int(coords[0]), int(coords[1])
    if x > -18 and x < 18 and y > -36 and y < 36:
        print("Bullet Time!")
    else:
        print("Time Flies!")
