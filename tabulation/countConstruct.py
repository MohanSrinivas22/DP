def countConstruct(target, words):
    n=len(target)+1
    ans=[0 for _ in range(n)]
    ans[0]=1
    for val in range(n):
        for word in words:
            m=val+len(word)
            if target[val:m]==word:
                ans[m]+=ans[val]
    print(ans)
    return ans[n-1]

print(countConstruct('abcdef', ['ab','abc','abcd','def','cd']))     # 1
print(countConstruct('purple', ['purpl','purp','ur','le','p']))     # 2
