from random import randint
a = 10 # Length of password
c = 100 # Number of password
def passgen(c,a): # first arg nubmer of pass, second arg length
    f = open('output.txt', 'w')
    for k in range(0,c): # Cycle with c
        for i in range(0,a): # Cycle with a
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
        l = str(k+1)
        print(l+"."+psw) # Print password formatting "sn.password"
        f.write(psw + '\n')
        del(psw) # clear string for next password
passgen(a,c)
