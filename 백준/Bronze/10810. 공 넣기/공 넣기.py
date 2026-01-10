n, m = map(int, input().split())

arr = [0] * n

for i in range(m):
    a,b,c = map(int, input().split())
    for i in range(a-1, b):
        arr[i] = c
        
for num in arr:
    print(num, end=' ')
