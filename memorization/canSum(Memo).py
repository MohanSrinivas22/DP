def canSum(targetSum, nums, memo):
    if targetSum in memo : return memo[targetSum]
    if targetSum < 0 : return False
    if targetSum == 0 : return True
    for num in nums:
        rem=targetSum-num
        if canSum(rem, nums, memo):
            memo[targetSum] = True
            return True
    return False

print(canSum(7, [2], {}))
print(canSum(7, [2,3,5,7], {}))

# Sample output :-
'''False
True'''
