def solve(n):    
    a = list(map(int,input().split()))
    a.sort()
    print(a)
    sum = 0
    for i in range(1,n+1):
        print("e", a[i])
        print("sum", sum)
        print("i", i)
        sum += a[i-1]
        if sum != i:
            print(i)
            break
    return 

n = int(input())
solve(n)



