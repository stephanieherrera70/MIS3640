age = input('What is your age?')
age= int(age)

if age >=18:
    print('Your age is {}.'.format(age))
    print('Adult')
elif age >=6:
    print('Teenager')
else: #CAN'T FORGET COLON!!!
    print('Kid')

