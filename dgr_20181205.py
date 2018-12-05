Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> orginal = "To be or not be"
>>> type(orginal)
<class 'str'>
>>> orginal [0]
'T'
>>> orginal [1]
'o'
>>> orginal [2]
' '
>>> orginal [3]
'b'
>>> ord(orginal [0])
84
>>> bin(ord(orginal [0]))
'0b1010100'
>>> bin(ord(orginal [0])) ^ key
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    bin(ord(orginal [0])) ^ key
NameError: name 'key' is not defined
>>> key = 5
>>> (ord(orginal [0])) ^ key
81
>>> chr(ord(orginal [0]) ^ key)
'Q'
>>> orginal
'To be or not be'
>>> key
5
>>> message = ""
>>> N = len(orginal)
>>> for i in range(N):
	message = message + chr(ord(orginal[i]) ^ key)

	
>>> message
'Qj%g`%jw%kjq%g`'
>>> result = ""
>>> key1 = 6
>>> for i in range(N):
	result = result + chr(ord(message[i]) ^  key1)

	
>>> result
'Wl#af#lq#mlw#af'
>>> result = ""
>>> key1 = 5
>>> for i in range(N):
	result = result + chr(ord(message[i]) ^  key1)

	
>>> result
'To be or not be'
>>> 
