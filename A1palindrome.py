#Recursive function isPalindrome

def isPalindrome(string): #name of the function
    if len(string) <= 2 : #If a word is a letter or two letters, it is palindrome.
        return True #True means that the word is Palindrome
    if string[0] != string[-1]: #If the first letter of the word [0] is not equal to the last letter of the word [-1], 
        return False #The word is not palindrome and it is false
    return isPalindrome(string[1:-1]) #it is a recurring process. After the first and last letter, then you check if the second letter and second to last letter are the same for a True statement, if not a false statement.

inputStr = input("Enter a string: ") #insert any word
print(isPalindrome(inputStr)) #this calls the function with a given word 