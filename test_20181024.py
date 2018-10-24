'''
#print('String Data Type')

str1 = "hello"
str2 = 'there'
bob = str1 + str2
print(bob)

str3 = 123
x = int(str3) + 1
print(x)

#print('Reading & Corventing')

name = raw_input('Enter:')
print(name)

apple = raw_input('Enter:')
x = apple - 10

apple = raw_input('Enter:')
x = int(apple) - 10
print(x)

#print('Looking Inside Strings')
fruit = 'banana'
letter = fruit[1]
print(letter)

x = 3
w = fruit[x - 1]
print(w)

#print('A Charter Too Far')
zot = 'abc'
print(zot[5])

#print('Strings Have Length')
#len Function
fruit = 'banana'
print len(fruit)
print(x)

#print('Looping Through Strings')
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

#print('Looping Through Strings')
fruit = 'banana'
for letter in fruit:
    print(letter)

#print('Looping and Counting')
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

#print('Looking Deeper into in')
for letter in 'banana':
    print(letter)

#print('Slicing Strings')
s = 'Monty Python'
#print(s[0:4])
#print(s[6:7])
#print(s[6:20])
#print(s[:2])
#print(s[8:])
#print(s[:])

#print('String Concatenation')
a = 'Hello'
b = a + 'There'
print(b)
c = a + ' ' + 'There'
print(c)

#print('Using in as a Logical Operator')
fruit = 'banana'
'n' in fruit
'm' in fruit
'nan' in fruit
if 'a' in fruit:
    print('Found it!')
'''
#print('String Comparison')

if word == 'banana':
    print('All right, bananas.')

if word < 'banana':
    print('Your word,', + word + ',comes before banana.')
elif word > 'banana':
    print('Your word,', + word + ',comes after banana.')
else:
    print('All right, bananas.')
    

