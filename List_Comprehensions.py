import time
x=int(input())
y=int(input())
z=int(input())
n=int(input())
i=0
j=0
k=0
a=[]
b=[]
while i<=x:
    j=0
    while j<=y:
        k=0
        while k<=z:
            b=[i,j,k]
            a.append(b)
            k+=1
        j+=1
    i+=1
l=1
while l!=0:
    l=0
    for c in a:
        d=sum(c)
        if d==n:
            a.remove(c)
            l=1
print(a)