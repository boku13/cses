#gfg
def getSubSeq(s, n):
    res = ""
    cr = 0
    while (cr < n):
         
        mx = s[cr]
        for i in range(cr + 1, n):
            mx = max(mx, s[i])
        lst = cr
 
        for i in range(cr,n):
            if (s[i] == mx):
                res += s[i]
                lst = i
 
        cr = lst + 1
     
    return res

def solve():
    n = int(input())
    s = input()
    print(getSubSeq(s))
    
    
for _ in range(int(input())):
    solve()