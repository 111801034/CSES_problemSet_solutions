
def DFS(start):
    queue = []
    queue.append(start)
    visited_list[start] = "True"
    while queue:
        s = queue.pop(0)
        row = int(s/m)
        column = int(s%m)
        for action in adjacent_list[s]:
            if action == "up":
                if row-1 >=0 and building[row-1][column] == ".":
                    if visited_list[(row-1)*m+column] == "False":
                        queue.append((row-1)*m+column)
                        visited_list[(row-1)*m+column] = "True"
            elif action == "down":
                if row+1 < n and building[row+1][column] == ".":
                    if visited_list[(row+1)*m+column] == "False":
                        queue.append((row+1)*m+column)
                        visited_list[(row+1)*m+column] = "True"
            elif action == "left":
                if column-1 >=0 and building[row][column-1] == ".":
                    if visited_list[(row)*m+column-1] == "False":
                        queue.append((row)*m+column-1)
                        visited_list[(row)*m+column-1] = "True"
            elif action == "right":
                if column+1 < m and building[row][column+1] == ".":
                    if visited_list[(row)*m+column+1] == "False":
                        queue.append((row)*m+column+1)
                        visited_list[(row)*m+column+1] = "True" 
                


n,m = input().split()
n = int(n)
m = int(m)
building = []
for i in range(0,n):
    temp = input()
    building.append(temp)
adjacent_list = {}
visited_list = {}
for i in range(0,n):
    for j in range(0,m):
        if building[i][j] == ".":
            adjacent_list[i*m + j] = ["up","down","left","right"]
            visited_list[i*m + j] = "False"
ans = 0
for i in range(0,n):
    for j in range(0,m):
        if building[i][j] == "." and visited_list[i*m+j] == "False":
            ans = ans + 1
            DFS(i*m+j)
print(ans)
            
  


