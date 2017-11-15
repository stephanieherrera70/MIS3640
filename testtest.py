 x = number
        y = 10
        tens = (x-x%y)/y
        digits = x%y
        if digits == 0:
            return trans[str(tens)] + " " + trans[str(y)]
        if tens == 1:
            return trans[str(y)] + " " + trans[str(digits)]
        return trans[str(tens)] + " " + trans[str(y)] + " " + trans[str(digits)]