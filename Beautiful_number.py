

n = input()
n = int(n)
even_str = ""
odd_str = ""
if n == 1:
    print("1")
elif n < 4:
    print("NO SOLUTION")
else:
    for i in range(2,n+1,2):
        print(str(i),end=" ")
    for i in range(1,n+1,2):
        print(str(i),end=" ")
