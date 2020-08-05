
T = input()
T = int(T)
for t in range(0,T):
    n = input()
    n = int(n)
    weights = list(map(int,input().split()))
    weights.sort()
    if n == 1:
        print(0)
    else:
        a = weights[0] + weights[1]
        b = weights[-1] + weights[-2]
        ans = 0
        for s in range(a,b+1):
            visited = []
            pairs = 0
            for i in range(0,n-1):
                for j in range(i+1,n):
                    if weights[i] + weights[j] == s and i not in visited and j not in visited:
                        pairs = pairs + 1
                        visited.append(i)
                        visited.append(j)
            if pairs > ans:
                ans = pairs
        print(ans)


