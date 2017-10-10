#nested list
#print([10,20,30,40])

AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
numbers = [42, 123]
empty = []
print(AFC_east, numbers, empty)

AFC_east[3] = 'New York Giants'
print(AFC_east)

print(AFC_east[-1])

print('Buffalo Bills' in AFC_east)

L = [
         ['Apple', 'Google', 'Microsoft'],
         ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
         ['Adam', 'Bart', 'Lisa']
    
]
#On Rail
print(L[1][2][1])
#Lisa
print([-1][-1])

for team in AFC_east:
    print(team)

numbers = [2, 0, 1, 6, 9]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    
print(numbers)

my_list = ['spam', 1, ['New England Patriots', \
                       'Buffalo Bills', 'Miami Dolphins', \
                       'New York Giants'], \
           [1, 2, 3]]
print(len(my_list))

print(len(my_list[2]))

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

print(['Tom Brady', 'Bill Belichick']*3)

t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3])

print(t[:5])

print(t[3:])

print(t[-3:])

print(t[:])

t = ['a', 'b', 'c', 'd', 'e', 'f']

print(t.append('g'))

print(t.append('g','h','i','j'))

print(t.extend(a))

#map, reduce and filter

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

print(only_upper('Babson College'))

