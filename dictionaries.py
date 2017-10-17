#names = ['Julian', 'Zach', 'Alex']
#scores = [95, 75, 85]

#grades = {} # can also use dict()
#grades['Zach'] = 75
#grades
#def histogram(s):
 #   d = dict()
  #  for c in s: 
   #     if c not in d: 
    #        d[c] = 1
     #   else: 
      #      d[c] += 1
    #return d

#print(histogram('Bookkeeper'))

#def histogram(s):
#    d = dict()
#    for c in s.lower(): # all lowercase for bookkeeper 
#        if c not in d: 
#            d[c] = 1
#        else: 
#            d[c] += 1
#    return d

#print(histogram('Bookkeeper')) 

#print(sorted(h))

def histogram(s):
    d = dict()
    for c in s.lower: 
        d[c]= d.get(c, 0) + 1
    return d

h = histogram('Bookkeeper')
print(h) 

def print_hist():
    for c in h: 
        print(c, h[c])

print_hist()

for key in sorted(h):
    print(key, h[key])

d = cword.txt
for k, v in s:
    if v not in d[k]: # if value not in list already
        d[k].append(v)