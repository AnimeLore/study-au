def factorial(x):
    out = x
    x -= 1
    while x != 0:
        out *= x
        x -= 1
    return out
x = int(input())
y = 3
out = x
for i in range(0,100):
    out += (x**y)/factorial(y)
    y+=2