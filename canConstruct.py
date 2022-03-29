def canConstruct(target, wordBank, memo={}):
    if target == '': return True
    if target in memo: return memo[target]
    for word in wordBank:
        if target.startswith(word):
            if canConstruct(target.replace(word,'',1),wordBank, memo):
                memo[target]=True
                return True
    memo[target]=False
    return False

print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(canConstruct('eeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee']))
print(canConstruct('purple', ['purp', 'le', 'p', 'p', 'ur']))

# Output :-
'''
True
False
False
True
'''
