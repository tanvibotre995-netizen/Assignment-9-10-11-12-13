def digits(n):
    Count = 0
    while(n !=0):
            n=n//10
            Count= Count + 1
    print("Count of digits",Count)

def main():
    n=int(input("enter number:"))
    digits(n)

if __name__ == "__main__":
    main()
            
    
