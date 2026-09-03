n=int(input())
arr=list(map(int,input().split()))
positive=0
negative=0
zero=0
for i in arr:
    if i>0:
     positive+=1
    elif i<0:
     negative+=1
    else:
     zero+=1
print(f"{positive:.6f}")
print(f"{negative:.6f}")
print(f"{zero:.6f}")




