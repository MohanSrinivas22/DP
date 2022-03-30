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
