def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
        print(fact)


def main():
    n=int(input("enter number:"))
    factorial(n)

if __name__ == "__main__":
    main()
