n = int(input())

arr = []

for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

d1 = 0
d2 = 0

for i in range(n):
    d1 = d1 + arr[i][i]
    d2 = d2 + arr[i][n - 1 - i]

print(abs(d1 - d2))