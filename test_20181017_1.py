'''
#Repeat Steps
n =5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')
print(n)

#An infinite Loop
n = 5
while n > 0:
    print('Lather')
    print('Rinse')
print('Dry off!')

#Another Loop
n = 0
while n > 0:
    print('Lather')
    print('Rinse')
print ('Dry off!')

#Breaking Out of a Loop
while True:
    line = raw_input('>')
    if line == 'done' :
        break
    print(line)
print('Done!')

# Finishing an Interation with continue
while True:
    line = raw_input('>')
    if line[0] == '#' :
        continue
    if line == 'done':
        break
    print
print('Done!')

#A Simple Definite Loop
for i in [5,4,3,2,1] :
    print (i)
print ('Blastoff')

# A Definite Loop with Strings
friends = ['Joseph','Glenn','Sally']
for friend in friends :
    print('Happy New Year:', friend)
print('Done!')

#Looping Through a Set
print('Before')
for thing in [9,41,12,3,74,15]:
    print(thing)
print('After')

#Finding the Largest Value
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far,the_num)

print('After', largest_so_far)

#Counting in a Loop
zork = 0
print('Before',zork)
for thing in [9,41,12,3,74,15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)

#Summing in a Loop
zork = 0
print('Before', zork)
for thing in [9,41,12,3,74,15]:
    zork = zork + thing
    print(zork, thing)
print('After', zork)

#Finding the Average in a Loop
count = 0
sum = 0
print('Before', count, sum)
for value in [9,41,12,3,74,15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / count)

#Filtering in a Loop
print('Before')
for value in [9,41,12,3,74,15]:
    if value > 20:
        print('Large number',value)
print('After')

#Search Using a Boolean Variable
found = False
print('Before',found)
for value in [9,41,12,3,74,15]:
    if value == 3:
        found = True
    print(found, value)
print('After', found)

#How to find the Smallest Value
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far)

#Finding the Smallest Value
smallest_so_far = -1
print('Before', smallest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)

print('After', smallest_so_far)

#Finding the Smallest Value
smallest = None
print('Before')
for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)


#Tests Class - 10

largest = None
smallest = None
while True:
    inp = input("Ievadi skaitli:")
    if num == "done": break
    print(num)

print("Maximum", largest)
'''
largest = None
smallest = None
while True:
    inp = raw_input("Ievadi skaitli:")
    if inp == "done":
        break
    try:
        num = int(inp)
        if smallest is None:
            smallest = num
        elif num < smallest:
            smallest = num
        if largest is None:
            largest = num
        elif num > largest:
                largest = num
    except ValueError:
        print("Invalid input")
        #break
print("Maximum is", largest)
print("Minimum is", smallest)
