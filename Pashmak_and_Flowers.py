
from collections import Counter

n = input()
n = int(n)
beauty = list(map(int,input().split()))
beauty.sort()
hello = beauty[-1] - beauty[0]
ans = 0
hi = Counter(beauty)
if hi[beauty[0]] == n:
    ans = n*(n-1)
    ans = int(ans/2)
else:
    ans = (hi[beauty[0]]*hi[beauty[-1]])

print(hello,ans)
