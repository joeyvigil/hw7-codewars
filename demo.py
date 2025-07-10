def expanded_form(num):
    digits = list(str(num))
    output=""
    for x in range(len(digits), 0,-1):
        if (int(digits[len(digits)-x]) !=0):
            output=output+" + "+str(int((digits[len(digits)-x]))*(10**(x-1)))
        print(digits[len(digits)-x])
        print(10**(x-1))
        pass
    return output[3:]

print(expanded_form(70304))