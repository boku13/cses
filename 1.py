def solve():
    a, b = map(int, input().split())
    # print(a, b)
    
    ma = max(a,b)
    mi = min(a,b)
    
    if ma <= 2*mi:
        if (ma + mi)%3 == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")


for t in range(int(input())):
    solve()