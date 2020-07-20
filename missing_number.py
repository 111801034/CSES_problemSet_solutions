

n = input()
n = int(n)
store_the_elements = list(map(int,input().split()))
store_the_elements.append(n)
store_the_elements.sort()
for i in range(0,n):
    if store_the_elements[i] != (i+1):
        break
print(i+1)
