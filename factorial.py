def test(*args):
    print(args)

test(3, 'Hello!', [3,4,5])

def factorial(number):
    if number == 1:
        return number
    else:
        return number * factorial(number - 1)

print(factorial(9))