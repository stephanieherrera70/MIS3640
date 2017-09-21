weight = input('Enter you weight (in kg):')
height= input('Enter your height (in meter):')
weight = float(weight)
height = float(height)

bmi = weight / (height * height)

if bmi <= 18.5:
    print("your bmi is {:.1f}. You are underwight." .format(bmi))
else bmi > 18.5 and bmi <= 25:
    print("your bmi is {:.1f}. You are normal-weight." .format(bmi))
elif 25 < bmi <= 29.9:
    print("your bmi is {:.1f}. You are overweight." .format(bmi))
else: 
    print("your bmi is {:.1f}. You are obese." .format(bmi))


    