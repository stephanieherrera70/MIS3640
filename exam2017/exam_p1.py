trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si', '5':'wu', 
         '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi', '100': 'bai'}



def speak_Chinese(number):
    '''
    number: an integer, 0<=number<=999
    Returns: a string that is the number in Chinese
    '''
    if number < 0 or number >= 1000:
        return "I wish I knew more Chinese..."
    elif number <= 10:
        return trans[str(number)]
    elif number <= 99:
        x = number
        y = 10
        tens = (x - (x % y)) / y
        digits = x % y
        if digits == 0:
            return trans[str(tens)] + " " + trans[str(y)]
        elif tens == 1:
            return trans[str(y)] + " " + trans[str(digits)]
        else:
            return trans[str(tens)] + " " + trans[str(y)] + " " + trans[str(digits)]

    elif number <= 999:
        x = number
        y = 100
        z = 10
        hundreds = (x-x%y)/y
        hundred_amount = hundreds*y
        tens_amount = number - hundred_amount
        x = tens_amount
        tens = (x-x%z)/z
        digits = x%z

        if (tens == 0) and (digits == 0):
            return trans[str(hundreds)] + " " + trans[str(y)]
        elif tens == 0:
            return trans[str(hundreds)] + " " + trans[str(y)] + " " +trans[str(0)] + " " + trans[str(digits)]
        else:
            return trans[str(hundreds)] + " " + trans[str(y)] + " " + trans[str(tens)] + " " + trans[str(z)] + " " + trans[str(digits)]
    else:
        return "does not exist"


# For testing
def main():
    print(speak_Chinese(306))
    print('In Chinese: 36 = san shi liu')
    # print(speak_Chinese(20))
    # print('In Chinese: 20 = er shi')
    # print(speak_Chinese(16))
    # print('In Chinese: 16 = shi liu')
    # print(speak_Chinese(200))
    # print('In Chinese: 200 = er bai')
    # print(speak_Chinese(109))
    # print('In Chinese: 109 = yi bai ling jiu')
    # print(speak_Chinese(999))
    # print('In Chinese: 999 = jiu bai jiu shi jiu')

if __name__ == '__main__':
    main()