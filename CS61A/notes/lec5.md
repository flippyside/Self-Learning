# Environment

## function currying(函数柯里化)

> transforming a multi-argument fuction into a single-argument, higher-order function. 将一个接受两个参数的函数转化为一系列嵌套的单参数函数

```py
def curry2(f):
	def g(x):
		def h(y):
			return f(x,y)
		return h
	return g
```

```py
>>> m = curry2(add)
>>> add_three = m(3)
>>> add_three(2)
5
>>> curry2 = lambda f: lambda x: lambda y:f(x, y)
>>> m = curry2(add)
>>> m(2)(3)
5
```


```py
def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

curried_pow = curry2(pow)
two_to_the = curried_pow(2)
x = two_to_the(5)  """32"""
```

---


```py
def print_sums(n):
    print(n)
    def f(k):
        return print_sums(n + k)
    return f    
g = print_sums(1) """1""" # first call the print_sums(1), print(1), and return func f, which takes in k and calls print_sums(1 + k) and return its results. now g is f
h = g(3) """4""" # f(3) is called so print_sums(1 + 3) is called, print(4), and return func f, which takes in k and calls print_sums(4 + k) and return its results. now h is f
w = h(5) """9""" # f(5) is called so print_sums(4 + 5) is called, print(9), and return func f, which takes in k and calls print_sums(9 + k) and return its results. now w is f
```

the same thing:

```py
def print_sums(n):
    print(n)
    def f(k):
        return print_sums(n + k)
    return f    
print_sums(1)(3)(5)  """1 4 9"""
```

- line4 is returning the return of function "print_sums"
- line5 is returning the function "f"



```py
def f(x):
    me = 1
    def g(y):
        return me
    me = 2
    print(g(7))  """2"""
    return x + y
y = 1
z = f(2)
```
first me is 1, then me is assigned with 2, and print calls g(), so g return me, but me has been changed in the frame of f(x), so 2 is printed


## higher order lambda

```py
higher_order_lambda = lambda f : lambda x : f(x)
g = lambda x : x * x
higher_order_lambda(g)(2)  """4"""
```

- higher_order_lambda takes in f, and return a function that is "lambda x : f(x)".
- higher_order_lambda(g) means pass func g into f, and "lambda x : g(x)" is returned
- higher_order_lambda(g)(2) means pass 2 into x, and g(x) is returned, the result is 4.









