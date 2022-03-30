''' Fibonacci '''
def fib(n):
    fi=[0]*(n+1)
    fi[1]=1
    if n<2:return fi[n]
    for i in range(2,n+1):
        fi[i]=fi[i-1]+fi[i-2]
    return fi[n]

print(fib(1)) # 1
print(fib(6)) # 8
print(fib(8)) # 21
print(fib(50)) # 12586269025
