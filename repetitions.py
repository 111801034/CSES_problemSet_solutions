
Given_string = input()
break_points = []
ans = []
for i in range(0,len(Given_string)-1):
    if Given_string[i] != Given_string[i+1]:
        break_points.append(i)
for i in range(0,len(break_points)-1):
    ans.append(break_points[i+1] - break_points[i])
if break_points != []:
    ans.append(len(Given_string) - 1 - break_points[-1])
    ans.append(break_points[0]+1)
else:
    ans.append(len(Given_string))
ans.sort()
print(ans[-1])




