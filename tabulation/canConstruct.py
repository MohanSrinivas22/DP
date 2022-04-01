def canConstruct(target, words):
    n=len(target)+1
    ans=[False]*(n)
    ans[0]=True
    for val in range(n):
        if ans[val]:
            for word in words:
                if target[val:val+len(word)]==word:
                    ans[val+len(word)]=True
    return ans[n-1]

print(canConstruct('abcdef',['ab','abcd','abc','def','cd']))    # True
print(canConstruct('abcdefghi',['ab','abcd','abc','def','cd'])) # False
