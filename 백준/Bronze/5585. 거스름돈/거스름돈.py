n = int(input())

n = 1000 - n
coin_arr = [500, 100, 50, 10, 5, 1]

count = 0
for coin in coin_arr:
    count += n // coin
    n %= coin

print(count)