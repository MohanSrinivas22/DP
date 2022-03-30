''' Fibonacci '''
def fib(n):
    fi=[0]*(n+1)
    fi[1]=1
    if n<2:return fi[n]
    for i in range(2,n+1):
        fi[i]=fi[i-1]+fi[i-2]
    return fi[n]

print(fib(1)) # 1
print(fib(6)) # 8
print(fib(8)) # 21
print(fib(50)) # 12586269025



''' Grid Traveller '''
def gridTraveller(n,m):
    grid=[[0 for _ in range(m+1)] for _ in range(n+1)]
    grid[1][1]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            grid[i][j]=max(grid[i][j],grid[i][j-1]+grid[i-1][j])
    #print(grid)
    return grid[n][m]
    
print(gridTraveller(3,3))    # 6
print(gridTraveller(2,3))    # 3
print(gridTraveller(18,18))  # 2333603220



''' canSum '''
