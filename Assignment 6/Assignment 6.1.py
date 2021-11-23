#Program 1: Number Sorter
#Create a program that ask 4 numbers. 
a=int(input("Please enter your first number:"))
b=int(input("Please enter your second number:"))
c=int(input("Please enter your third number:"))
d=int(input("Please enter your fourth number:"))

#Print the 4 numbers from highest to lowest using only if-else statement.
def arrange():    
 if a> b and c and d:
    (first_number)=a
    return first_number
 if b>a and c and d:
    (second_number)=b 
    return second_number
 if c>a and b and d:
    (third_number)=c
    return third_number
 if d>a and b and c:
    (fourth_number)=d
    return fourth_number
first_number=a
second_number =b
third_number=c
fourth_number=d


print (f"{first_number},{second_number},{third_number},{fourth_number}")

