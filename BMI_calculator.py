def BMI(weight, height):
    bmi = 703 * weight / (height * height)


weight = input('What is your weight?')
weight = int(weight)

if weight <= 18.5:
    print('Your weight is {}.' .format(weight))
    print('Underweight')

elif weight === "18.5 - 24.9":
    print('Your weight is {}.' .format(weight))
    print('Normal weight')

elif weight === "25 - 29.9":
    print('Your weight is {}.' .format(weight))
    print('Overweight')

else:
    print(Obesity)

weight = input('Enter your weight (n lb):')
height = input('Enter your height (in in):')
weight = fload(weight)
height = float(height)
calculate 