b, n, m = map(int, input().split())
keyboards = list(map(int, input().split()))
usb = list(map(int, input().split()))

maximum = -1

for k in keyboards:
    for u in usb:
        total = k + u
        if total <= b:
            maximum = max(maximum, total)

print(maximum)