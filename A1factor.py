# Factoring of integers
integer = input('integer') #inserting your integer
n= int(integer) #integer form (numbers)

def factor(n): #defining/naming the function, has to end with ":"
    print('The integer is {}.'.format(integer)) #Printing what integer we are using.
    for i in range(1, n + 1): #This is beginning a loop, to continue getting more factors. 
        if n % i == 0: #We need to check which number divides the given number with zero remainder. For finding the remainder we use %. 
             print(i)
        
    

