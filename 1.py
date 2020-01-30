x = int(input())
y = 2
out = 1
for i in range(0,100):
    out -= x**y
    y += 2
    out += x**y
    y += 2