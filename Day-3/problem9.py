n = int(input())
arr = list(map(int, input().split()))

max_height = max(arr)
count = arr.count(max_height)

print(count)