

T = input()
T = int(T)
for t in range(0,T):
    n = input()
    n = int(n)
    candies = list(map(int,input().split()))
    oranges = list(map(int,input().split()))
    minimum_candies = min(candies)
    minimum_oranges = min(oranges)
    moves = 0
    for i in range(0,n):
        count = 0
        if candies[i] > minimum_candies:
            moves = moves + (candies[i] - minimum_candies)
            count = count + 1
        if oranges[i] > minimum_oranges:
            moves = moves + (oranges[i] - minimum_oranges)
            count = count + 1
        if count == 2:
            moves = moves - min(candies[i] - minimum_candies,oranges[i] - minimum_oranges)
    print(moves)
            
    

