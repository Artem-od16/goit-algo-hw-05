def caching_fibonacci():
    cache={}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif  n == 1:
            return 1
        elif n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# We get the fibonacci function
fib = caching_fibonacci()

# We use the fibonacci function to calculate Fibonacci numbers
print(fib(10)) # Print 55
print(fib(15)) # Print 610