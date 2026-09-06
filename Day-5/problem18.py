n, k = map(int, input().split())
bill = list(map(int, input().split()))
b = int(input())

total = sum(bill)
fair_share = (total - bill[k]) // 2

if b == fair_share:
    print("Bon Appetit")
else:
    print(b - fair_share)