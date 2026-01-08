a, b, c = map(int, input().split())

rslt = 0
if a == b and a == c and b == c:
    rslt = 10000 + a * 1000
elif a == b or a == c or b == c:
    if b == c:
        rslt = 1000 + b * 100
    else:
        rslt = 1000 + a * 100
else:
    maxValue = a
    if (maxValue < b): maxValue = b
    if (maxValue < c): maxValue = c
    rslt = maxValue*100

print(rslt)