#Program 1: Number Sorter
#Create a program that ask 4 numbers. 
a=int(input("Please enter your first number:"))
b=int(input("Please enter your second number:"))
c=int(input("Please enter your third number:"))
d=int(input("Please enter your fourth number:"))

#Print the 4 numbers from highest to lowest using only if-else statement.
#a    
def aprint():
 if a>= b and a>= c and a>=d:
    if b>=c and b>=d:
     if c>=d:
       print=a, b, c, d
    else:
        print=a, b, d, c
    if c>b:
      print=a, d, c, b
    else:
      print=a, d, b, c
    if c>= d and c>=b:
      if b>=d:
       print=a, c, b, d
    else:
       print=a, c, d, b
 return print

final=aprint()
print (final)
    
    




