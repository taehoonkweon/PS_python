a = int(input())
b = int(input())

rslt = 0
for i in range(b):
    price, num = map(int, input().split())
    rslt += (price*num)

if rslt == a:
    print("Yes")
else:
    print("No")