
T = input()
T = int(T)
for t in range(0,T):
    n = input()
    n = int(n)
    arr = list(map(int,input().split()))
    arr.sort()
    if n == 1:
        print("YES")
    else:
        count = -123
        for i in range(0,n-1):
            if arr[i+1] - arr[i] >= 2:
                count = i
                break
        if count != -123:
            print("NO")
        else:
            print("YES")