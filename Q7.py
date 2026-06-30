def Natural(n):
    sum = 0
    for i in range(1,n +1):
        sum = sum + i
        print(sum)

def main():
    n=int(input("enter the number:"))
    Natural(n)

if __name__ == "__main__":
    main()
