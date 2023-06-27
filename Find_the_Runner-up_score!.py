if __name__ == '__main__':
    import time
    n = int(input())
    arr = list(map(int,input().split()))
    b=max(arr)
    c=min(arr)
    a=arr[0]
    for i in arr:
        if a<i and i<b and i>0:
            a=i
        elif c<i and i<b and i<0:
            c=i
        else:
            if a==b:
                a=c    
    print(a)