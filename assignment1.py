#Factoring of integers
#integer = input('integer')
#n= int(integer)

#def factor(n):
#    print('The integer is {}.'.format(integer))
#    for i in range(1, n + 1):
#        if n % i == 0:
#             print(i)
        
    
#print(factor(50))
#print('The factors of',n,'are:')


#Recursive function isPalindrome

def isPalindrome(string):
    if len(string) <= 2 :
        return True 
    if string[0] != string[-1]:
        return False 
    return isPalindrome(string[1:-1])

inputStr = input("Enter a string: ")
print(isPalindrome(inputStr))


#The Drunkard's Walk 

#Use Turtle to draw the drunkard's walk 