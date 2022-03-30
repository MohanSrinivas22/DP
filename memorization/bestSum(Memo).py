def bestSum(target, nums, memo):
    if target in memo : return memo[target]
    if target == 0 : return []
    if target < 0 : return None
    best=None
    for num in nums:
        rem = target - num
        res = bestSum(rem, nums, memo)
        if res != None:
            temp = res + [num]
            if best == None or len(temp) < len(best):
                best = temp[:]
    memo[target] = best
    return best

print(bestSum(7, [5,3,4,7], {}))
print(bestSum(8, [1,4,5], {}))
print(bestSum(100, [1,2,5,25], {}))

# Sample output :-
'''[7]
[4, 4]
[25, 25, 25, 25]'''
