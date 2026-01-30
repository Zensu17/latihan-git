def fib():
    """Generate an infinite sequence of Fibonacci numbers."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

import types
if type(fib()) == types.GeneratorType:
    print("fib is a generator function")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter >= 10:
            break
else:
    print("fib is not a generator function")

