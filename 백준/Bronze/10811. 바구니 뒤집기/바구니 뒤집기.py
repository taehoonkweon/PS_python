n, m = map(int,input().split())

arr = [0]*n
tmp_arr = [0]*n

for i in range(n):
    arr[i] = i+1

for i in range(m):
    a, b = map(int,input().split())
    if (b-a == 0): continue
    elif (b-a == 1):
        tmp = arr[a-1]
        arr[a-1] = arr[b-1]
        arr[b-1] = tmp
    else:
        cnt = 1
        for j in range(n):
            tmp_arr[j] = arr[j]
        for j in range(a-1, b):
            arr[j] = tmp_arr[b-cnt]
            cnt += 1

for i in range(n):
    print(arr[i], end=' ')