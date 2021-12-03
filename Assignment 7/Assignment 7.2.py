#Program 2: Password validator
#Create a program that check if password is valid
#The password is valid if all criteria are met:
#a. Greater than 15 letters
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char (!@#$%^&*()_+ etc)
#ex.
#input: P@ssw0rd+P@ssw0rd
#ouput: Valid
print("The password must have: ")
print("at least one capital letter")
print("at least one number")
print("at least one special character")
print("and greater than 15 letters")

password=input("Please enter your password:")
pcount= len(password)

upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
uppercount=0
spcial="!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
spcialcount=0
num="0123456789"
numcount=0
lwr="abcdefghijklmnopqrstuvwxyz"
lowercount=0

pcount=len(password)
if pcount>15:
    for pwpord in password:
        if pwpord in upper:
            uppercount=uppercount +1
    for pwpord in password:
        if pwpord in spcial:
            spcialcount=spcialcount +1
    for pwpord in password:
        if pwpord in num:
            numcount=numcount +1
    for pwpord in password:
        if pwpord in lwr:
           lowercount=lowercount+1
if uppercount>=1 and spcialcount >=1 and numcount>=1 and (uppercount+spcialcount+numcount+lowercount==pcount):
    print("valid")
else:
    print("invalid")
