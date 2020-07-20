

n = input()
n = int(n)
array = list(map(int,input().split()))
turns = 0
for i in range(0,n-1):
    if array[i+1] >= array[i]:
        pass
    else:
        turns = turns + (array[i] - array[i+1])
        array[i+1] = array[i]
print(turns)