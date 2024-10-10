a=10
b=12
c=0
if a and b and c :
    print("All the numbers have Boolean value as True")
else:
    print("Atleast one number has Boolean value as True")
    
a=10
b=-10
c=0
if a>0 or b>0:
    print("Either of the number is greater  ")
else:
    print("no number is greater than zero")
    

if b>0 or c>0:
    print("either of the number is greater than zero")
else:
    print("no number is greater than zero")



a = 23
b = 24
c = 22


if a > b or a < c:
    print("I am using or operator")
elif a < b and a > c:
    print("I am using and operator")
