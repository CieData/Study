a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
a,b,c
try:
    ab=(b[1]-a[1])/(b[0]-a[0])
    bc=(c[1]-b[1])/(c[0]-b[0])
    if ab==bc:
        print(0)
    elif ab>bc:
        print(-1)
    else:
        print(1)
except:
    if b[0]==a[0] and c[0]==b[0]:
        print(0)
    # elif b[0]==a[0] and c[0]!=b[0]:
    #     c[1]-b[1]>=
ab
bc