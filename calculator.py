#program for Simple calculator
def add(): 
    a=int(input("Enter the  First number:"))
    b=int(input("Enter the Second number:"))
    add=a+b
    print("Sum of",a,"and",b,"is:",add)

def sub(): 
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))
    sub=a-b
    print("Subtraction of",a,"and",b,"is:",sub)  
def mul():
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:")) 
    mul=a*b
    print("Multiplication of",a,"and",b,"is:",mul)
    
def div(): 
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))
    if(b!=0):
        div=a/b
    else: 
        print("Cannot divide")
    print("Division of",a,"and",b,"is:",div)
    
def rem(): 
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))
    rem=a%b
    print("Reminder/Modulus of",a,"and",b,"is:",rem)
    


while True:
    print("\n\nHere is the simple Calulator")
    print("\nCalculation Menu:")
    print("--------------------------------")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulus")
    print("6.Exit")
    
    choice=int(input("Enter Your Choice(1-6):"))
    if choice==1:
        print("FOR ADDITION:\n")
        add()
    elif choice==2:
        print("FOR SUBTRACTION:\n")
        sub()
    elif choice==3:
        print("FOR MULTIPLICATION:\n")
        mul()
    elif choice==4:
        print("FOR DIVISION:\n")
        div()
    elif choice==5:
        print("FOR MODULUS:\n")
        rem()
    elif choice==6:
        print("Existing calculation menu. Goodbye!")
        break
    else:
        print("Please enter valid choice between 1 to 6!")