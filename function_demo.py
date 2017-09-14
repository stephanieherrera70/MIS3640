def print_lyrics():
    print ("Hey Jude. Don't make it bad.")
    print ("Take a sad song and make it be better.")

print_lyrics()

print(type(print_lyrics))

def repeat_lyrics():
    print_lyrics()
    print('Na - na - na - na - na - na - na')
    print_lyrics()

repeat_lyrics()

def print_twice(name):
    print(name)
    print(name) 

print_twice('Andrew')

def my_abs(number):
    print(abs(number))

my_abs(-40)

def give_me_a_break():
    str1 = 'break'
    return str1

print(give_me_a_break())

def give_me_a_break():
    str1 = 'break'
    return str1
    print('another break')
    
print(give_me_a_break())

result = print_twice('Bing')
print(result)

#how?
def my_abs(number):
    str1 = -40
    return str1
    print(abs(str1))

my_abs(-40)

def nop():
    pass




import math
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

#Exercise 1 
def quadratic(a, b, c, x):
    y = ((a*x)**2 + b*x + c)
    return y
answer = quadratic(4, 6, 3, 2)
print(answer)