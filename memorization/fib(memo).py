def fib(n,memo):
  if n in memo:return memo[n]                   # memo is our memorization object.
  if n<=2:return 1                              # memo is of dictionary type.           
  memo[n]=fib(n-1,memo)+fib(n-2,memo)
  return memo[n]

print(fib(1,{}))
print(fib(2,{}))
print(fib(3,{}))
print(fib(4,{}))
print(fib(5,{}))
print(fib(10,{}))
print(fib(300,{}))
