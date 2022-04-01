def bestSum(target, nums):
    ans=[None]*(target+1)
    ans[0]=[]
    for val in range(1,target+1):
        for num in nums:
            rem=val-num
            if rem==0:ans[val]=ans[0]+[val];break
            elif rem>0 and ans[rem]!=None:
                temp=ans[rem]+[num]
                if ans[val]==None or len(temp)<len(ans[val]):
                    ans[val]=temp[:]
    print(ans)
    return ans[target]

print(bestSum(7, [5,3,4,7])) # [7]
print(bestSum(8, [2,1,5,3])) # [3,5]
print(bestSum(8, [1,2]))     # [2,2,2,2]
print(bestSum(7, [2,4]))     # None
print(bestSum(300, [7,14]))  # None
