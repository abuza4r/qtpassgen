from random import randint
def passgen(a): # first arg len,
    for i in range(0,a): # Cycle for len
        b = randint(0,2) # Choose number or letter
        if b == 0:
            if i == 0:
                psw = chr(48+randint(0,9))
            else:
                psw +=chr(48+randint(0,9))
        elif b == 1:
            if i == 0:
                psw = chr(97+randint(0,25))
            else:
                psw +=chr(97+randint(0,25))
        elif b == 2:
            if i == 0:
                psw = chr(65+randint(0,25))
            else:
                psw += chr(65+randint(0,25))
    return psw
