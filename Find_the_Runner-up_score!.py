if __name__ == '__main__':
    import time
    n = int(input())
    arr = list(map(int,input().split()))
    b=max(arr)
    c=min(arr)
    for i in arr:
        if c<=i and i<b:
            c=i
    print(c)