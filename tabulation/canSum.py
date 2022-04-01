def canSum(target, nums):
    ans=[False]*(target+1)
    ans[0]=True
    for val in range(1,target+1):
        for num in nums:
            rem=val-num
            if rem>=0 and ans[rem]:ans[val]=ans[rem];break
    # print(ans)
    return ans[target]

print(canSum(7, [5,3,4,7])) # True
print(canSum(300, [7,14]))  # False
