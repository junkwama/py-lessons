# Python Notes

## 1. Data types in python

In python the type of a variable is dynamic depending on the value given. 
Ex: `name = "sdds"` is `str` but can become `int` once we do `name=32`.

The keywords `str`, `int`, `float`, `bool`, `list`, `complex`, `tuple`, `dict`, `set`, `range` represent variable types. Ex: `print(type([1,2]) == list)` returns true. 
They are also class constructors. So they can be used to create variables of specific types. Ex: `float(2)` creates a float variable.
They can also be used for casting (converting) variable types. Ex: `age = "12"; age = int(age)` => converts `str` to `int`.

Notes:
- The global function `type(var)`: returns the type of the variable it receives as a parameter.
- We can also use the `isinstance(var, type)` function to check if a variable is an instance of a type class `type`.

### 1.A STRING

Notes:
- We can use the three quotation notation to define a multiline string. 
    Ex: 
    ```python
    var = """ 
    - Judy
    - Noella
    - Astrid
    - Pdjo
    """  
    ```
- The `+=` operator works also for string concatenation. Ex: `name = "ju"; name += "dy"` # name equals "judy".
- We can add an "f" right before the quotations of a string to inject some variable into the string.
- Built-in methods of strings don't alter the original string; they all return a brand new string.

Built-in methods:

- `"".upper()`: converts to uppercase. `islower()`: to check if all letters are lower.
- `"".lower()`: converts to lowercase. `isupper()`: to check if all letters are in uppercase.
- `"".title()`: makes the first letter of every word capital. `istitle()`: to check if every first letter is capital.
- `strip`, `isalnum`, `isdecimal`, `isalpha`, `split`, `find`, `startswith`, `endswith`, `replace`, etc.

We can use the `len()` global function to count the number of characters.
We can also use the `in` operator instead of the `.find()` method. Ex: `"JU" in "JUDY"` returns true.
To get a substring from a string we can also use brackets. Ex: `sentence = "my son is coming". sentence[3:6]` returns "son".

### 1.B COMPLEX NUMBERS

num1 = 1+2j
num2 = complex(1,2)

`print(num1.real)` -> prints 1.0 as the real num part
`print(num1.imag)` -> prints 2.0 as the imaginary parts 

NOTE: Both the real and imag parts are handled as floats

#### Global functions to work with numbers:
    `- abs(num)`: return the absolute value of a num. Ex abs(-3.5) returns 3.5
    `- round(5.5, decimal precision)`: return 6

### 1.C ENUMS

Enums are readable names bound to constant values. It is the only way to create constants in python.
To use enums we need to import the Enum class from the enum module: from enum import Enum

```python
class NameToGiveToTheEnum(Enum):
    CONST_NAME1 = val1
    CONST_NAME2 = val2
    CONST_NAME3 = val3
```

To get the value: 
    - NameToGiveToTheEnum.CONST_NAME.value
    - NameToGiveToTheEnum["CONST_NAME"].value
To get the const name:
    - NameToGiveToTheEnum(val)
    - NameToGiveToTheEnum["CONST_NAME"]

    The list(NameToGiveToTheEnum): global function lists all the values of the Enum
    len(NameToGiveToTheEnum): to count the number of constants it has

### 1.D LISTS

- We can use [x:y]: to get a range of items from a list. Ex [:4] from index 0 to 4 (excluded); [3:6] from 3 (included) to 6 (excluded)
- Methods of list modify the existing array
        
#### Methods:

- `list.append(ele)` to add ele to the end of the list
- `list.insert(index, val)`: To add an element in the middle of a list
- `list1.extend([list2])` merges list1 with list2. It is also a way to add elements to a list
- Instead of extend we can also use the += operator
- We can add many elements in the middle of a list by using range operator: `list[3:3] = [4, "Uot", 6]`
- `list.remove(eleValue)`: find the ele and removes it. Breaks the code if the ele is not found
- `list.pop()`: remove and returns the last ele
- `reverse`, `sort`, `copy` ..etc

The global function sorted(list, key=str.lower) returns the sorted list without modifying it, so it does it by copying the original. key=str.lower for case insensitiveness

    ## 1.F. Tuples

Ex: tuple = (ele1, ele2, ele3,...)

Tuples look like list but they are created with parentheses. 
Tuple are immutable. The can't be modified.
The accep most of the lists' function: len, sorted

```python
tuple[1] # ele2
tuple.index(ele2) # 1
newTuple = tuple + (1, 3, 4)
```

## 1.G. Dictionaries
```python
person = {
    "name" : "Judy",
    "height": 1.9
    "black_eyes": true    
}
```
    person["key"] to access a prop of a Dict (read and write)
    person.get("key", "alternativvalue) (read only)ts and wanna modify it

    To add a new key, you do as if it exis

#### Built in methodes:
- `.pop("key_to_remove")`
- `.popitem()`: to remove the last inserted element
- `.items()`: returns a list of tuples with 2 element each: the first of is the key and second one value
- `.keys()`, `.values()`
- `in` operator can be used to check in a key exists in a dict 
- `del dict["key"]` to delete a key

## 1.H. Sets

myset = { 1, 3, 4, "roger" }

So they are kind of list but created with curly braces

Sets are mathematical sets. With all the operations we can perform on mathematical sets.
Notes:
     - In a set we can't have the same element twice. 



## 2. Operators

### 2.A. Arithmetic Operators:
```python
    +, -, *, /, %, **, //: # flore division that does the division and rounds the answer down
    *=, +=, -=, //= etc...
```

### 2.B. Comparison Operators
```python
    ==, >, <, >=, <=, !=
```

### 2.C. Logical Operators

`and`, `or`,`not`

Note: 
- `or` can be used in a serie of expressions to return the first none true expression or otherwise return the last expression
- So it can be used for ternary operators. Ex: sold = 0 or 1 #sold  will be 1
- `and` can also be used in a series of expression to return the first falsy expression otherwise return the last expression
- So it can be used for ternary operators. Ex: sold = 0 or 1 #sold  will be 0
        
### 2.D. IN and IS Operators

`in`: is used to check if a value is contained in a list or in a sequence
`is`: is used to check if two object represent the same object

### 2.E. Ternary Operator

In python the ternary operator is implemented with if else alined on the same line:
    var = ValForTrue if condition else ValForFalse
    Ex: state = "adult" if age >= 18 else "underaged"

### 2.F any and all global function.
They are both used with list or sequences.
- any[ele1, ele2,...] return true is even one of the elements of the sequence is true
- all[ele1, ele2,...] return true only if all the elements of the sequence are true


## 3. User Inputs

We use the input("text") global function to receive input from user.
Ex: name = input("Type your name: ")

## 4. Control Statements

### 4.A. if elif elif else
```python
if (cond):
    instructions
elid (cond):
    instructions
else:
    instructions

### 4.B. While
    while cond:
        instructions
```

### 4.C. For in loop

```python
for item in list:
    print(item) # instructions
```
```python
    for item in range(10):
        print(item) # instructions
```
- `range(offset)`: function returns a list with elements from 0 to offset
```python
    for (index, item) in enumerate(list):
        print(index, item) # instructions
```

- `enumerate(list)` function implemented with for in loop heps extract the index of items in the loop
we can use continue nad break statement in python as well
        
## 5. Functions
```python
def fx_name(params="default value"):
    # instructions
    return expression
```

In python we can nest functions on inside an other. This is useful we wanna separate a part of code that is useful only to a specific function.
But when from a nested function we want to access a var defined in the parent function we need to reference that var inside the nested function using:
"nonlocal var_name".

Since we can define functions in other function we can also return a function from a function. This gives birth to the idea of Clausures.
In python, a returned child function can keep track on the variables of the parent funciton even when the parent function is no longer active. This is called Clausures.

Notes: 
    - In python, a function can return more than one element. All elements will be returned in a tuple in that case.

### 5.A. Lambda functions

Lambda functions are comparable to Js's arrow function. 
- They are sigle line fx
- Can receive x params
- Always return a value
- They can be asigned to a variable to be called later on.

Ex:
```python 
pow2 = lambda n: n * n
pow2(5) returns 25
```

### 5.B. Useful global function

#### 5.B.1 Map(), Filter(), Reduce()
- `map(fx, list)`: fx: The func to apply on each item; list the list of items to transform
- `filter(fx, list)`: if the item make fx return True, the the item is taken otherwise the item is thrown away
- `reduce(fx, list)`: it returns a value calculated by evaluating items of the list. Ex: for findin' the sum of a list elements.

### 5.C. Dcorator Functions

Decorator funcitions are functions' that add additional features to a fx
They can be used to determined a dynamic part of a function. They recive a function, wrape it into a wrapper and return a new one.
They can be used to run the same code on multiple function

Note  
- reduce is not global, it needs to be imported from the functools lib
- It's very comon to use lambda function in map, filter and reduce()
- These 3 funct need to be cast with list() to get a list

```python
# the decorator fx
def decorator_fx(fx):
    def wrapper():
        name = fx()
        print(f"Hello {name}")
    return wrapper

# Passing to the decorator function a fx as param:
@decfx
def hello():
    name = input("Enter your name :")
    return name

# Calling the wrapped fx
hello()
```

### 5.D. List Comprehensions

List comprehension is a smarter way of mapping or going through a list.
Syntax: `new_list = [operation_to_apply_on_each_ele for var_used_in_the_operation in old_list]`

## 6. Classes

Names of classes start with capital letter. 
Every function defined in a class to be used as method should have "self" as first argument. "self" keyword points to the current object of the class.
`__init__` is the constructor method of a class

```python
class Person:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
    
    def introduce(self):
        print(f"Hi! my name is {self.name}. I am a {'man' if self.sex == 'm' else 'woman'}")
judy = Person("Judy", "m")
judy.introduce()
```

### 6.A. Inheritance

Inheritance is done by putting the inherited class between parenthesis in class definition.
If the parent class receives constructor params, we need to call it inside the child's constructor with the necessary params

```python
class Being:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    
    def introduce(self):
        print(f"Hi! my name is {self.name}. I am a {'male' if self.gender == 'm' else 'female'}")

class Human(Being):
    def __init__(self, name, gender, profession):
        Being.__init__(self, name, gender)
        self.profession = profession

class Animal(Being):
    def __init__(self, name, gender):
        Being.__init__(self, name, gender)

    def bark(self):
        print("Barking...")

class MyChildClass(MyParentClass):
    # instructions
```

### 6.B. Operation Overloading

In Python, we can define what happens when two objects are *, -, / or compared, etc., using operator overloading special functions inside the class definition of the objects.

`__gt__(self, other):`
    return True if self.xprop > other.xprop else False
`__add__(self, other):`
    self.sold += other.sold 

`__lt__`: less than
`__sub__`: -
`__mul__`: *
`__truediv__`: /
`__floordiv__`: //
`__mod__`: %
`__pow__`: **


## 7. Modules

In python every file is a module and everything inside it (function, class, vars) are exported automatically.
So we just need to import a file using it name to access everything inside it.

__**In file_2**__
```python
import file_1
file_1.func()
```

We can also import one specific function or anything instead of importing the whole file

__**In file_2**__
```python
from file_1 import func
func()
```
Notes:
- When we put our .py files in a sub folder, to import the as module we need to add a empty file named `__init__.py.`
This will tell python that our subfolder contains py modules.
- Python has many buit in libs for extra functionalities: 
- fuctools: a lib that provide useful functions like reduce()
math, statitistics, random, http, requests, html, sqlite3, re (regex), json, datetime, os (operating system), urllib

## 8. Command line arguments

import sys
print sys.argv # list of received arguments with the first one automatically "~path/name_of_file.py"

## 9. Others

### 9.A. DocString
""" doc string """ They are kind of python's special coment, that can be transformed into code documentation. They follow specific standars and can extend to multiple lines

### 9.B. Annotation
A way to inforce functions or bound variables a pecific type

Ex:

```python
my_var: int = 3; def my_func() -> int: 
```

### 9.C. Exception handling

```python
try:
    # tricky code
except ZeroDivisionError:
    # what to do if a Zero division error occures
except XError:
    # what to do if a x error occures
except:
    # what to do if any diff error occures
else:
    # what to do if no error occures
finally:
    # code to run whatever happens. (Err or no err)
```

We throw an error using:
    raise `Exception("message)`
```python
try:
    raise Exception("message")
except Exception as error:
    print(error)
```

### 9.D. with keyword

very useful can for exemple allow to open a file with carring about closing it

Ex:

```python
with file_content = open("path", "r")
print(file_content)
```