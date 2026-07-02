def perfect(n):
    sum=0
    for i in range(1,n):
        if(n % i==0):
            sum = sum +i

    if sum == n:
        print("Perfect Number")
    else:
        print("Not Perfect Number")

def main():
    n=int(input("enter number:"))
    perfect(n)

if __name__ == "__main__":
    main()

    
