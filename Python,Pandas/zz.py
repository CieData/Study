n,s=map(int,input().split())
a=list(map(int,input().split()))
b=[0]*(n+1)
c=[0]*(n+1)
for j in range(1,len(a)):
    x=sum(a[j+1])
    if x>=s:
        b[0]=x
        c[0]=j
        break
for i in range(1,len(a)):
    x=b[i-1]-a[i-1]
    if x>=s:
        b[i]=x
        c[i]=c[i-1]-1
    else:
        for j in range(c[i-1],len(a)):
            x+=a[j]
            if x>=s:
                b[i]=x
                c[i]=j-i
                break
print(min(c))
    


