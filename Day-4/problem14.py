n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0

for num in range(max(a), min(b) + 1):
    if all(num % x == 0 for x in a) and all(y % num == 0 for y in b):
        count += 1

print(count)