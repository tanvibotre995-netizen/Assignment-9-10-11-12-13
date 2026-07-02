def factor(n):
    for i in range(1,n+1):
        if(n % i ==0):
            print(i)

def main():
    n=int(input("enter number:"))
    factor(n)

if __name__ == "__main__":
    main()
