def binary(n):
    while(n>0):
        print(n %2)
        n=n//2

def main():
    n=int(input("enter number:"))
    binary(n)

if __name__ == "__main__":
    main()
