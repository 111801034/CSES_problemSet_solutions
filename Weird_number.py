
n = input()
n = int(n)
ans = str(n)
while(n != 1):
    if n%2 == 0:
        n = n/2
    else:
        n = 3*n + 1
    n = int(n)
    ans = ans + " " + str(n)
print(ans)