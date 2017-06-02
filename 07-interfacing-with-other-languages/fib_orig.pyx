def fib(n):
    a,b = 1,1
    for i in range(n):
        a,b = a+b, a
    return a