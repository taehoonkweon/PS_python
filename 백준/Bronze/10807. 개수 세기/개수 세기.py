a = int(input())

num_arr = list(map(int, input().split()))

compare = int(input())
cnt = 0

for num in num_arr:
    if compare == num:
        cnt += 1
    
print(cnt)