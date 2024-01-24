def dfs(lab, i, j, res, sol):
    # print(res)
    # print(i, j)
    if lab[i][j] == 'B':
        print(sol)
        res.append(sol)
        return
    
    lab[i][j] = '#'
    if i-1 >= 0:
        if lab[i-1][j] != '#':
            new = sol + "U"
            dfs(lab, i-1, j, res, new)
    if i+1 < len(lab):
        if lab[i+1][j] != '#':
            new = sol + "D"
            dfs(lab, i+1, j, res, new)
    if j-1 >= 0:
        if lab[i][j-1] != '#':
            new = sol + "L"
            dfs(lab, i, j-1, res, new)
    if j+1 < len(lab[0]):
        if lab[i][j+1] != '#':
            new  = sol + "R"
            dfs(lab, i, j+1, res, new)
        
# lab = np.zeros()
m, n = map(int, input().split())

lab = [list(input()) for i in range(m)]
# print(lab[1][2])
res = []
for i in range(m):
    for j in range(n):
        if lab[i][j] == 'A':
            dfs(lab, i, j, res, "")

print(res)

if len(res) != 0:
    fin = res[0]
    min = len(res[0])
    for ans in res:
        if len(ans) < min:
            fin = ans
            min = len(ans)
    print("YES")
    print(min)
    print(ans)
else:
    print("NO")