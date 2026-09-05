s, t = 7, 11
a, b = 5, 15

apples = [-2, 2, 1]
oranges = [5, -6]

apple_count = 0
orange_count = 0

for x in apples:
    position = a + x
    if s <= position <= t:
        apple_count += 1

for x in oranges:
    position = b + x
    if s <= position <= t:
        orange_count += 1

print(apple_count)
print(orange_count)