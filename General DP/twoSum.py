def twoSum(nums, target):
    d={}
    for i,j in enumerate(nums):
        rem=target-j
        if rem in d and d[rem]!=i:
            return [d[rem],i]
        d[j]=i
    return []

print(twoSum([3,3],6))          # [0,1]
print(twoSum([3,2,4],6))        # [1,2]
print(twoSum([2,7,11,15],9))    # [0,1]
