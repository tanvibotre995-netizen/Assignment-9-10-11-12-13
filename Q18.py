def calculate(No1,No2):
    Addition = No1 +No2
    print("addition is",Addition)

    Substraction = No1 - No2
    print("Substraction is",Substraction)

    Multiplication = No1 *No2
    print("Multiplication is",Multiplication)

    Division = No1 /No2
    print("Division is",Division)

def main():
    No1=int(input("enter number:"))
    No2=int(input("enter number:"))

    calculate(No1,No2)
    
if __name__ == "__main__":
    main()
