def digits(n):
    Sum = 0
    while(n !=0):
        digit = n % 10      
        Sum = Sum + digit  
        n = n // 10

    print("Sum of digits",Sum)

def main():
    n=int(input("enter number:"))
    digits(n)

if __name__ == "__main__":
    main()
            
    
