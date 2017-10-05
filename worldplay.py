fin = open('words.txt')

#line = fin.readline()
#print(line)

#for line in fin:
#    word = line.strip()
#    print(word)

#for line in fin:
#    word = line.strip()    
#    if len(word) > 20:
#        print(word, len(word))

#def has_no_e(word):
#    for letter in word: 
#        if letter == 'e':
#             return False
    
#    return True 

#print(has_no_e('Babson'))

#easier way to do this
#def has_no_e(word): 
#return not 'e' in word.lower()

#for all words with no e in a loop
#def fine_words_no_e():
#    fin = open('words.txt')
    # two variable , counter for no e and counter for other words 
#    counter_no_e= 0
#    counter_total = 0 

#    for line in fin:
#        counter_total +=1
#        word = line.strip()
#        if has_no_e(word):
#            #print(word)
#            counter_no_e +1=
#    return counter_no_e/counter_total

def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True 


print(avoids('Babson','abcd'))
print(avoids('College','ab'))
    
#input is forbidden for secnd part of 3 

#Exercise 1.4

def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

#print(uses_only('a hole face', ' acefhlo'))

#Exercise 1.5

def uses_all(word, required):
    for letter in required:
        if letter in word:
            return True
    return False

#print(uses_all('tomot', 'mot'))

def uses_all(word, required):
    return uses_only(required, word)

#Exercise 1.6

def is_abecedarian(word):
    previous = [0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

# Exercise 2

def is_abecedarian1(word):
    previous = [0]
    iteration = 1
    while iteration > previous:
        for letter in word:
            return True
            iteration += 1
            previous += 1    
    return False

print(is_abecedarian1('alry'))'
Chat Conversation End
Type a message...







