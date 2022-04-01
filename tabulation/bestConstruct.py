def bestConstruct(target, words):
    n=len(target)+1
    ans=[None]*(n)
    ans[0]=[]
    for val in range(n):
        for word in words:
            if target[val:val+len(word)]==word and ans[val]!=None:
                temp=ans[val]+[word]
                m=val+len(word)
                if ans[m]==None or len(temp)<len(ans[m]):
                    ans[m] = temp
    print(ans)
    return ans[len(target)]

print(bestConstruct('abcdef', ['ab','abc','abcd','def','cd']))  # ['abc', 'def']
print(bestConstruct('purple', ['purpl','purp','ur','le','p']))  # ['purp', 'le']
