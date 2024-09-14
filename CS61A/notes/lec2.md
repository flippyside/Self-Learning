## Type of expressions

An expression describes a computation and evaluates to a value
All expressions can use function call notation
所有表达式都可以使用函数调用符号


```python
# Call expressions
max(2, 3)
min(1, -2, 3, -4, 5)
pow(100, 2)
pow(2, 100)

# Imports built-in functions and built-in names
from math import pi  //makes the name pi available
pi * 71 / 223
from math import sin
sin(pi/2)

# Assignment
radius = 10  //intialize radius to 10
2 * radius
area, circ = pi * radius * radius, 2 * pi * radius
radius = 20

# Function names
max
max(3, 4)
f = max
f   //now f can do the thing that max can do
f(3, 4)
max = 7  
f(3, 4)
f(3, max)
f = 2
# f(3, 4)
__builtins__.max

# User-defined functions
from operator import add, mul

def square(x):
    return mul(x, x)

square(21)
square(add(2, 5))
square(square(3))

def sum_squares(x, y):
    return add(square(x), square(y))
sum_squares(3, 4)
sum_squares(5, 12)

# area function
def area():
    return pi * radius * radius
area()
radius = 20
area()
radius = 10
area()

# Name conflicts
def square(square):
    return mul(square, square)
square(4)
```

**Primitive expressions**:
- Number or Numeral  `2`
- Name  `add`
- String  ``'hello'``

**Call expressions**:

  `max     ( 2    ,   3 ) `
Operator Operand   Operand

an operand can also be a call expression:
`max(min(pow(3, 5), -4), min(1, -2))`

---

**Environment Diagrams**

visualize the interpreter’s process.

Execution rule for assignment statements:
1. Evaluate all expressions to the right of = from left to right.
2. Bind all names to the left of = to those resulting values in the current frame.

tools:
[Python Tutor](https://pythontutor.com/cp/composingprograms.html#mode=edit)

```python
>>> a=1
>>> b=2
>>> b, a = a+b, b   //execute a+b and b first,then assign them to b and a
>>> a
2
>>> b
3
```

Defining Functions:

Function signature indicates how many arguments a function takes

```python
>>> def <name>(<formal parameters>):
		return <return expression>
```

Looking Up Names In Environments

Every expression is evaluated in the context of an environment.

So far, the current environment is either:
- The global frame alone, or
- A local frame, followed by the global frame.

Most important two things:
An environment is a sequence of frames.
A name evaluates to the value bound to that name in the earliest frame of the current environment in which that name is found.

E.g., to look up some name in the body of the square function:
- Look for that name in the local frame first.
- If not found, look for it in the global frame.
(Built-in names like “max” are in the global frame too,but we don’t draw them in environment diagrams.)

Formal Parameter形参

a formal parameter is a variable used in the definition of a function to receive the actual parameters passed in when the function is called.
formal parameters are meaningful ONLY ==within the scope of the function body==,and are used to implement the code.

```python
def sum_squares(x, y):
    return square(x) + square(y)

result = sum_squares(3, 4)
```
x,y are formal parameters
3,4 are actual parameters

When the function `sum_squares` is called, the formal parameter `x` receives the value of the actual parameter `3`, and the formal parameter `y` receives the value of the actual parameter `4`. Then, within the function body, these formal parameter values are used to execute the function's logic.

```python
from operator import mul
def square(square):
    return mul(square,square)  //within the function,square is -2
square(-2)
```

Analogy: frame is like { } in c++
		 local variables & global variables,BUT global variable will not be changed when local variables are changed!

```python
>>> x = 12
>>> def f(y):
...     x = 3
...     print(x)
...
>>> f(7)
3
>>> print(x)
12
```

x is like two different people, same name: one is inside the f,the other is outside. a imaginary and virtual world! when u can't find x in this world, check the other world.