a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=0
y=0
for i in range(3):
    if a[i]>b[i]:
        x+=1
    elif a[i]<b[i]:
        y+=1
print(x,y)