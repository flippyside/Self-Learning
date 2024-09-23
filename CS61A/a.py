def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

curried_pow = curry2(pow)
two_to_the = curried_pow(2)
x = two_to_the(5)
print(x)


