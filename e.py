# Team 32

lines = []

with open("e.in", 'r') as File:
    lines = File.readlines()

total = lines.pop(0)

for line in lines:
    stock = line.split()
    for item in range(len(stock)):
        stock[item] = int(stock[item])
    days = stock.pop(0)
    price = []
    for day_i in range(days+1):
        for day_j in range(days+1):
            if day_i <= day_j:
                # print(day_i, day_j)
                price.append(sum(stock[day_i:day_j+1]))
    print(max(price))
