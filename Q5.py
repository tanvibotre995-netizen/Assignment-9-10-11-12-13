def Divide(n):
    if n % 3 == 0  and n % 5 == 0:
        print("divisible by 3 and 5")
    else:
        print("not divisible")

def main():
        n = int(input())
        Divide(n)

if __name__ == "__main__":
     main()

    
