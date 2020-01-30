x = int(input())
out = 1
y = 1
y1 = 3
for i in range(0,100):
    out -= (x**y)/y1
    y += 1
    y1+= 2
    out += (x**y)/y1
    y += 1
    y1 += 2
