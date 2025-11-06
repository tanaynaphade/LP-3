# Fibonacci using Recursion and Iteration

def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n-1) + fib_rec(n-2)

def fib_iter(n):
    a, b = 0, 1
    print(a, b, end=" ")
    for _ in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c
    print()

n = int(input("Enter number of terms: "))

print("\nRecursive Fibonacci:")
for i in range(n):
    print(fib_rec(i), end=" ")

print("\n\nIterative Fibonacci:")
fib_iter(n)
