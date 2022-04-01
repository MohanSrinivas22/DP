def howSum(target, nums):
    ans=[None]*(target+1)
    ans[0]=[]
    for val in range(1,target+1):
        for num in nums:
            rem=val-num
            if rem==0:ans[val]=ans[0]+[val];break
            elif rem>0 and ans[rem]!=None:
                ans[val]=ans[rem]+[num];break
    # print(ans)
    return ans[target]

print(howSum(7, [5,3,4,7])) # True
print(howSum(7, [2,4]))     # False
print(howSum(300, [7,14]))  # False
