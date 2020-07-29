
from collections import Counter
import math

n = input()
n = int(n)
A = list(map(int,input().split()))
a = Counter(A)
most_occured_one = a.most_common(1)
if most_occured_one[0][1] > math.floor(n/3):
    print(most_occured_one[0][0])
else:
    print(-1)
