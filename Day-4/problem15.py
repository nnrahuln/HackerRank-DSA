n = int(input())

scores = list(map(int, input().split()))

highest = scores[0]
lowest = scores[0]

high_count = 0
low_count = 0

for score in scores[1:]:
    if score > highest:
        highest = score
        high_count += 1

    if score < lowest:
        lowest = score
        low_count += 1

print(high_count, low_count)