


```python
print(x)
```

Run code in VScode terminal:
```powershell
PS D:\code> cd python #cd : go to the file
PS D:\code\python> python welcome_to_CS61A.py # python filename.py to run code
5
PS D:\code\python> python -i  welcome_to_CS61A.py
5
>>>          # you can interact with your code now!
```

```python
# Numeric expressions
2020
2000 + 20
-1 + 2 + 3 + 4 * ((5 // 6) + 7 * 8 * 9)

# Functions
abs(-2)
abs(2301 - 4321)

# Values
"Go Bears"
"Gob" + "ears"

# Objects
shakes = open('shakespeare.txt')
text = shakes.read().split()
len(text)
text[:25]
text.count('the')
text.count('thou')
text.count('you')
text.count('forsooth')
text.count(',')

# Sets
words = set(text)
len(words)

# Combinations 
'draw'
'draw'[0]
{w[0] for w in words}

# Data
'draw'[::-1]
{w for w in words if w == w[::-1] and len(w)>4}
{w for w in words if w[::-1] in words and len(w) == 4}
{w for w in words if w[::-1] in words and len(w) > 6}

``` 

