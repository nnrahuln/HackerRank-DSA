n = int(input())
birds = list(map(int, input().split()))

count = {}

for bird in birds:
    count[bird] = count.get(bird, 0) + 1

max_count = max(count.values())

# If tie, choose the smallest bird type
answer = min(bird for bird in count if count[bird] == max_count)

print(answer)