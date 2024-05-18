def test(*args):
    print(args)

test(3, 'Hello!', [3,4,5])

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

print(factorial(9))
