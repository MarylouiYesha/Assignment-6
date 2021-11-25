#Program 1: Number Sorter
#Create a program that ask 4 numbers. 
a=int(input("Please enter your first number:"))
b=int(input("Please enter your second number:"))
c=int(input("Please enter your third number:"))
d=int(input("Please enter your fourth number:"))

#Print the 4 numbers from highest to lowest using only if-else statement.

#a    
if (a> b and a> c and a>d):
      #b second higest
      if (b>c and b>d and c>d):
            print(f"{a}, {b}, {c}, {d}")
      else:
            if (b>c and b>d and d>c):
                  print(f"{a}, {b}, {d}, {c}")
      #c seecond highest
      if (c>b and c>d and b>d):
            print(f"{a}, {c}, {b}, {d}")
      else:
            if(c>b and c>d and d>b):
                  print(f"{a}, {c}, {d}, {b}")
      #d second higest
      if (d>b and d>c and b>c):
            print(f"{a}, {d}, {b}, {c}")
      else:
            if(d>b and d>c and c>b):
                  print(f"{a}, {d}, {c}, {b}")
#b
if (b>a and b>c and b>d):
      #a second highest
      if (a>c and a>d and c>d):
            print(f"{b}, {a}, {c}, {d}")
      else:
            if (a>c and a>d and d>c):
                  print(f"{b}, {a}, {d}, {c}")
      #c second highest
      if (c>a and c>d and a>d):
            print(f"{b}, {c}, {a}, {d}")
      else:
            if (c>a and c>d and d>a):
                  print(f"{b}, {c}, {d}, {a}")
      #d second highest
      if (d>a and d>c and c>a):
            print(f"{b}, {d}, {c}, {a}")
      else:
            if(d>a and d>c and a>c):
                  print(f"{b}, {d}, {a}, {c}")

#c
