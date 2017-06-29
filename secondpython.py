#first lesson 06/28/17

'''multiple
line
comment'''
#single line comment
'''num = raw_input('Enter number')
num = int(num)#convert to integer
#for-loop
for i in range (1, num + 1):
    print i
#while-loop
    n = 1
    while n <= num :
        print n
        n = n + 1 #i++ will not work'''
'''for i in range (0 , 101, 10) : #(start, stop + 1, multiple)
    print i'''
'''for i in range(10, 0, -1):
    print i'''
'''for i in range (100, -5, -5) :
    print i'''

#second lesson 06/29/17
#groceries = ["Eggs", "Milk", "Butter", "Onion", "Apples"]
'''print groceries[4]

print groceries[1:4]

print groceries [:4]

print groceries [3:]

print groceries [0:5:2]'''

'''print len(groceries)

groceries.index('Apples')'''

'''
>>> name.lower
<built-in method lower of str object at 0x0000000003D417E0>
>>> name.lower()
'jennifer'
>>> name.upper()
'JENNIFER'
>>> name.capitalize()
'Jennifer'
>>> sentence = "what will I have for dinner?"
>>> sentence
'what will I have for dinner?'
>>> sentence.capitalize
<built-in method capitalize of str object at 0x0000000003C78830>
>>> sentence.capitalize()
'What will i have for dinner?'
>>> name[7]
'r'
>>> name.replace('e', 'a')
'Jannifar'
>>> name.replace('i', 'i'*5)
'Jenniiiiifer'
>>> name.replace('e', 'a', 1)
'Jannifer'
'''
'''for i in groceries :
    print i'''

'''#define a function

def say_hello( ) :
    print 'Hello!'
    print 'It\'s Thursday!'

def print_info(text):
    print 'Value is ' + text

#define cal_power
def cal_power(base, power):
    answer = 1
    for i in range(power):
        answer *= base
    return answer
    
say_hello()
print_info('June is almost over!')
print_info('What is your plan for July 4th?')

print cal_power(4, 2)
print cal_power(3, 5)

b = raw_input('Enter base: ')
p = raw_input('Enter power: ')
print cal_power(int(b), int(p))

import math

print math.pow(4,5)'''

'''groceries_by_price = {
    'Eggs' : 2.59,
    'Milk' : 3.19,
    'Butter' : 2.69,
    'Yogurt' : 3.19
    }
print groceries_by_price['Eggs']
for item in groceries_by_price:
    print item + " " + str(groceries_by_price[item])'''

def create_box(width, height) :
    for i in range(height):
        print '#' * width
w = raw_input('Enter width: ')
h = raw_input('Enter heigh: ')

create_box(int(w), int(h))
