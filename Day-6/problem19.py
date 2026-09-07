n = int(input())
p = int(input())

front = p // 2
back = (n // 2) - (p // 2)

print(min(front, back))