def howConstruct(target, words):
    n=len(target)+1
    ans=[None]*(n)
    ans[0]=[]
    for val in range(n):
        for word in words:
            if target[val:val+len(word)]==word and ans[val]!=None:
                ans[val+len(word)] = ans[val]+[word]
    print(ans)
    return ans[len(target)]

print(howConstruct('abcdef', ['ab','abc','abcd','def','cd']))   # ['abc','def']
