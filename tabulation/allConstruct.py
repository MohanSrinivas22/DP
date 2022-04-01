def allConstruct(target, words):
    n=len(target)+1
    ans=[[] for _ in range(n)]
    ans[0]=[[]]
    for val in range(n):
        for word in words:
            m=val+len(word)    
            if target[val:m]==word and ans[val]!=[]:
                for j in ans[val]:
                    temp=j+[word]
                    ans[m].append(temp)
    # print(ans)
    return ans[n-1]
                
    print(ans)
    return ans[n-1]

print(allConstruct('abcdef', ['ab','abc','abcd','def','cd'])) 
print(allConstruct('purple', ['purpl','purp','ur','le','p']))
print(allConstruct('', ['purpl','purp','ur','le','p']))
print(allConstruct('purplei', ['purpl','purp','ur','le','p']))

# [['abc', 'def']]
# [['purp', 'le'], ['p', 'ur', 'p', 'le']]
# [[]]
# []
