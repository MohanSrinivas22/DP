def allConstruct(target, wordBank, memo={}):
    if target in memo: return memo[target]
    if target == '': return [[]]
    ans=[]
    for word in wordBank:
        if target.startswith(word):
            rem=target.replace(word, '', 1)
            res=allConstruct(rem, wordBank, memo)
            for i,j in enumerate(res):
                res[i]=[word,*res[i]]
            if res!=[]: ans.extend(res) 
    memo[target]=ans
    return ans
        
print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(allConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(allConstruct('purple', ['purp', 'le', 'purpl', 'p', 'ur']))
print(allConstruct('eeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee']))
print(allConstruct('', ['abc', 'eeee', 'eeeee']))

# Output :-
'''
[['abc', 'def']]
[]
[['purp', 'le'], ['p', 'ur', 'p', 'purp', 'le']]
[]
[[]]
'''
