def howSum(targetSum, nums, memo):
    if targetSum in memo : return memo[targetSum]
    if targetSum == 0 : return []
    if targetSum < 0 : return None
    for num in nums:
        rem = targetSum - num
        res = howSum(rem, nums, memo)
        if res != None : 
            memo[targetSum] = res + [num]
            return memo[targetSum]
    memo[targetSum]=None
    return None

print(howSum(7, [2], {}))
print(howSum(7, [2,3,5,7], {}))

# Sample output :-
'''None
[3, 2, 2]'''
