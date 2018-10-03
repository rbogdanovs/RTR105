Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> a=2
>>> a
2
>>> vars ()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 2, '__package__': None}
>>> 10a
SyntaxError: invalid syntax
>>> a10

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a10
NameError: name 'a10' is not defined
>>> a 10
SyntaxError: invalid syntax
>>> a=10
>>> a
10
>>> 10 a
SyntaxError: invalid syntax
>>> print(123)
123
>>> print(98.6)
98.6
>>> print('Hello world')
Hello world
>>> print(class)
SyntaxError: invalid syntax
>>> print(as)
SyntaxError: invalid syntax
>>> print

>>> print(none)

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(none)
NameError: name 'none' is not defined
>>> x = 12.2
>>> y = 14
>>> vars ()
{'a': 10, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 12.2, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> x = 100
>>> vars ()
{'a': 10, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 100, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> spam

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    spam
NameError: name 'spam' is not defined
>>> Spam

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    Spam
NameError: name 'Spam' is not defined
>>> print(spam)

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(spam)
NameError: name 'spam' is not defined
>>> print(Spam)

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(Spam)
NameError: name 'Spam' is not defined
>>> print(SPAM)

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(SPAM)
NameError: name 'SPAM' is not defined
>>> print(eggs)

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(eggs)
NameError: name 'eggs' is not defined
>>> _speed

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    _speed
NameError: name '_speed' is not defined
>>> x1q3z9ocd = 35.5
>>> x1q3z9afd = 12,50
>>> x1q3z9ocd = 35,5
>>> x1q3p9afd = x1q3z9ocd * x1q3z9afd

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    x1q3p9afd = x1q3z9ocd * x1q3z9afd
TypeError: can't multiply sequence by non-int of type 'tuple'
>>> x1q3p9afd = x1q3z9ocd * x1q3z9afd

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    x1q3p9afd = x1q3z9ocd * x1q3z9afd
TypeError: can't multiply sequence by non-int of type 'tuple'
>>> x1q3z9ocd = 35.5
>>> x1q3z9afd = 12.50
>>> x1q3p9afd = x1q3z9ocd * x1q3z9afd
>>> print(x1q3p9afd)
443.75
>>> a
10
>>> x1q3z9ocd = 35.5
>>> x1q3z9afd = 12.50
>>> x1q3p9afd = x1q3z9ocd * x1q3z9afd
>>> print(x1q3p9afd)
443.75
>>> x = 2
>>> x = x + 2
>>> print(x)
4
>>> x = 3.9*x*(1-x)
>>> x
-46.8
>>> x = 3.9 * x * (1-x)
>>> x
-8724.455999999998
>>> x = 3.9 * x * ( 1 - x )
>>> x
-296886942.1125503
>>> x = 0.6
>>> x = 3.9 * x * ( 1 - x )
>>> x
0.9359999999999999
>>> xx = 2
>>> xx = xx + 2
>>> print(xx)
4
>>> yy = 440 * 12
>>> print(yy)
5280
>>> zz = yy / 1000
>>> print(zz)
5
>>> print(zz)
5
>>> jj = 23
>>> kk = jj %5
>>> print(kk)
3
>>> print(4**3)
64
>>> x = 1 + 2 * 3 - 4 / 5 ** 6
>>> x
7
>>> x = 1 + 2 ** 3 / 4 * 5
>>> print(x)
11
>>> ddd = 1 + 4
>>> print(ddd)
5
>>> eee = 'hello' + 'there'
>>> print(eee)
hellothere
>>> eee = 'hello' + 'there'
>>> eee = eee + 1

Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    eee = eee + 1
TypeError: cannot concatenate 'str' and 'int' objects
>>> type('hello')
<type 'str'>
>>> type(eee)
<type 'str'>
>>> type(1)
<type 'int'>
>>> xx = 1
>>> type (xx)
<type 'int'>
>>> temp = 98.6
>>> type(temp)
<type 'float'>
>>> type(1)
<type 'int'>
>>> type(1.0)
<type 'float'>
>>> print(float(99) + 100)
199.0
>>> i = 42
>>> type(i)
<type 'int'>
>>> f = float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(10/2)
5
>>> print(9/2)
4
>>> print(9/2.)
4.5
>>> print(99/100)
0
>>> print(99/100.)
0.99
>>> print(10.0/2.0)
5.0
>>> print(99.0/100.0)
0.99
>>> sval = '123'
>>> type(sval)
<type 'str'>
>>> print(sval + 1)

Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    print(sval + 1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival = int(sval)
>>> type(ival)
<type 'int'>
>>> print(ival + 1)
124
>>> nsv = 'hello bob'
>>> niv = int(nsv)

Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    niv = int(nsv)
ValueError: invalid literal for int() with base 10: 'hello bob'
>>> nam = input('Who are you?')
Who are you?

Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    nam = input('Who are you?')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> nam = input('Who are you?')
Who are you?r&b

Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    nam = input('Who are you?')
  File "<string>", line 1, in <module>
NameError: name 'r' is not defined
>>> nam = input('Who are you?')
Who are you?rainers

Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    nam = input('Who are you?')
  File "<string>", line 1, in <module>
NameError: name 'rainers' is not defined
>>> print('Weclome'.nam)

Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    print('Weclome'.nam)
AttributeError: 'str' object has no attribute 'nam'
>>> print('Welcome'.nam)

Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    print('Welcome'.nam)
AttributeError: 'str' object has no attribute 'nam'
>>> print('Welcome', nam)

Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    print('Welcome', nam)
NameError: name 'nam' is not defined
>>> nam = input('Who are you?')rainers
SyntaxError: invalid syntax
>>> print('Welcome', nam)

Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    print('Welcome', nam)
NameError: name 'nam' is not defined
>>> nam = input('Who are you?')
Who are you?"nam"
>>> print('Welcome', "nam")
('Welcome', 'nam')
>>> Rainers = input('Who are you?')
Who are you?"Rainers"
>>> print('Welcome', "Rainers")
('Welcome', 'Rainers')
>>> inp = input('Europe floor?')
Europe floor?"0"
>>> usf = int(inp) + 1
>>> print('US floor',"usf")
('US floor', 'usf')
>>> print(US floor,"usf")
SyntaxError: invalid syntax
>>> print('US floor',usf)
('US floor', 1)
>>> 
KeyboardInterrupt
>>> Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> a=2
>>> a
2
>>> vars ()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 2, '__package__': None}
>>> 10a
SyntaxError: invalid syntax
>>> a10

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a10
NameError: name 'a10' is not defined
>>> a 10
SyntaxError: invalid syntax
>>> a=10
>>> a
10
>>> 10 a
SyntaxError: invalid syntax
>>> print(123)
123
>>> print(98.6)
98.6
>>> print('Hello world')
Hello world
>>> print(class)
SyntaxError: invalid syntax
>>> print(as)
SyntaxError: invalid syntax
>>> print

>>> print(none)

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(none)
NameError: name 'none' is not defined
>>> x = 12.2
>>> y = 14
>>> vars ()
{'a': 10, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 12.2, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> x = 100
>>> vars ()
{'a': 10, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 100, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> spam

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    spam
NameError: name 'spam' is not defined
>>> Spam

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    Spam
NameError: name 'Spam' is not defined
>>> print(spam)

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(spam)
NameError: name 'spam' is not defined
>>> print(Spam)

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(Spam)
NameError: name 'Spam' is not defined
>>> print(SPAM)

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(SPAM)
NameError: name 'SPAM' is not defined
>>> print(eggs)

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(eggs)
NameError: name 'eggs' is not defined
>>> _speed

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    _speed
NameError: name '_speed' is not defined
>>> x1q3z9ocd = 35.5
>>> x1q3z9afd = 12,50
>>> x1q3z9ocd = 35,5
>>> x1q3p9afd = x1q3z9ocd * x1q3z9afd

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    x1q3p9afd = x1q3z9ocd * x1q3z9afd
TypeError: can't multiply sequence by non-int of type 'tuple'
>>> x1q3p9afd = x1q3z9ocd * x1q3z9afd

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    x1q3p9afd = x1q3z9ocd * x1q3z9afd
TypeError: can't multiply sequence by non-int of type 'tuple'
>>> x1q3z9ocd = 35.5
>>> x1q3z9afd = 12.50
>>> x1q3p9afd = x1q3z9ocd * x1q3z9afd
>>> print(x1q3p9afd)
443.75
>>> a
10
>>> x1q3z9ocd = 35.5
>>> x1q3z9afd = 12.50
>>> x1q3p9afd = x1q3z9ocd * x1q3z9afd
>>> print(x1q3p9afd)
443.75
>>> x = 2
>>> x = x + 2
>>> print(x)
4
>>> x = 3.9*x*(1-x)
>>> x
-46.8
>>> x = 3.9 * x * (1-x)
>>> x
-8724.455999999998
>>> x = 3.9 * x * ( 1 - x )
>>> x
-296886942.1125503
>>> x = 0.6
>>> x = 3.9 * x * ( 1 - x )
>>> x
0.9359999999999999
>>> xx = 2
>>> xx = xx + 2
>>> print(xx)
4
>>> yy = 440 * 12
>>> print(yy)
5280
>>> zz = yy / 1000
>>> print(zz)
5
>>> print(zz)
5
>>> jj = 23
>>> kk = jj %5
>>> print(kk)
3
>>> print(4**3)
64
>>> x = 1 + 2 * 3 - 4 / 5 ** 6
>>> x
7
>>> x = 1 + 2 ** 3 / 4 * 5
>>> print(x)
11
>>> ddd = 1 + 4
>>> print(ddd)
5
>>> eee = 'hello' + 'there'
>>> print(eee)
hellothere
>>> eee = 'hello' + 'there'
>>> eee = eee + 1

Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    eee = eee + 1
TypeError: cannot concatenate 'str' and 'int' objects
>>> type('hello')
<type 'str'>
>>> type(eee)
<type 'str'>
>>> type(1)
<type 'int'>
>>> xx = 1
>>> type (xx)
<type 'int'>
>>> temp = 98.6
>>> type(temp)
<type 'float'>
>>> type(1)
<type 'int'>
>>> type(1.0)
<type 'float'>
>>> print(float(99) + 100)
199.0
>>> i = 42
>>> type(i)
<type 'int'>
>>> f = float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(10/2)
5
>>> print(9/2)
4
>>> print(9/2.)
4.5
>>> print(99/100)
0
>>> print(99/100.)
0.99
>>> print(10.0/2.0)
5.0
>>> print(99.0/100.0)
0.99
>>> sval = '123'
>>> type(sval)
<type 'str'>
>>> print(sval + 1)

Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    print(sval + 1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival = int(sval)
>>> type(ival)
<type 'int'>
>>> print(ival + 1)
124
>>> nsv = 'hello bob'
>>> niv = int(nsv)

Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    niv = int(nsv)
ValueError: invalid literal for int() with base 10: 'hello bob'
>>> nam = input('Who are you?')
Who are you?

Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    nam = input('Who are you?')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> nam = input('Who are you?')
Who are you?r&b

Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    nam = input('Who are you?')
  File "<string>", line 1, in <module>
NameError: name 'r' is not defined
>>> nam = input('Who are you?')
Who are you?rainers

Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    nam = input('Who are you?')
  File "<string>", line 1, in <module>
NameError: name 'rainers' is not defined
>>> print('Weclome'.nam)

Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    print('Weclome'.nam)
AttributeError: 'str' object has no attribute 'nam'
>>> print('Welcome'.nam)

Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    print('Welcome'.nam)
AttributeError: 'str' object has no attribute 'nam'
>>> print('Welcome', nam)

Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    print('Welcome', nam)
NameError: name 'nam' is not defined
>>> nam = input('Who are you?')rainers
SyntaxError: invalid syntax
>>> print('Welcome', nam)

Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    print('Welcome', nam)
NameError: name 'nam' is not defined
>>> nam = input('Who are you?')
Who are you?"nam"
>>> print('Welcome', "nam")
('Welcome', 'nam')
>>> Rainers = input('Who are you?')
Who are you?"Rainers"
>>> print('Welcome', "Rainers")
('Welcome', 'Rainers')
>>> inp = input('Europe floor?')
Europe floor?"0"
>>> usf = int(inp) + 1
>>> print('US floor',"usf")
('US floor', 'usf')
>>> print(US floor,"usf")
SyntaxError: invalid syntax
>>> print('US floor',usf)
('US floor', 1)
>>> 
KeyboardInterrupt
>>> 

