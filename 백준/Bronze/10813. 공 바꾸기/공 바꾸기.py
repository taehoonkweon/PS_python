n, m = map(int, input().split())

arr = [0]*n

for i in range(n):
    arr[i] = i+1
    #print(arr[i], end=' ')

for i in range(m):
    a, b = map(int, input().split())
    tmp = arr[a-1]
    arr[a-1] = arr[b-1]
    arr[b-1] = tmp
    
for i in range(n):
    print(arr[i], end=' ')