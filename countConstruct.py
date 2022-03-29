def countConstruct(target, wordBank, memo={}):
    if target in memo: return memo[target]
    if target == '': return 1
    count=0
    for word in wordBank:
        if target.startswith(word):
            rem=target.replace(word, '', 1)
            count+=countConstruct(rem, wordBank, memo)
    memo[target]=count
    return count
        
print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(countConstruct('purple', ['purp', 'le', 'purpl', 'p', 'ur']))
print(countConstruct('eeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee']))

# Output :-
'''
1
0
2
0
'''
