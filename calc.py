#Session 1: Exercise 2
x = 60
y = x * 42
s = 42
print(y + s)
#2562 seconds

x = 1.61
print(10 / 1.61)
#6.211180 miles

print(2562/6.211180)
#412.482 seconds per mile

print(42/60)
42.7/6.211180
#6.874700000000 minutes per mile

print(42.7/60)
#0.711666666 hours

print(6.211180124/0.711666666666)
#8.727653703376

#Session 2: Exercise 1
#Volume of sphere
pi = 3.14
print((4/3)*pi*5*5*5)
#Total Wholesale cost for 60 copies
print(24.95 * .40 + 3 + .75 *59)
#What time do I get home for breakfast?
print((8 * 1 + 15 / 60) + ((7 * 3) + 3 * (12 / 60)) + (8 + 15 / 60))
#percentage of the increase 
print(((89-82)/82) * 100 + 'xx.x%') 

#Session 3
import time
date= time.time()
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(date)))

#in class overview 
import time
print(time.time())
current = time.time()
second = current % 60
minutes = (current// 60) % 60
hours = (current // 60) // 60 % 24
days = (current// 60) // 60 % 40 
print('Current time: %d days, %d hours, %d minutes, %d seconds from Epoch.' % (days, hours, minutes, seconds))

