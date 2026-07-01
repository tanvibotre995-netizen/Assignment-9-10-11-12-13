def prime(n):
    for i in range(2,n):
        if(n % i == 0):
            print("number is not prime")
            return
    print("number is prime")
      
def main():
    n=int(input("enter number:"))
    prime(n)

if __name__ == "__main__":
    main()



    
