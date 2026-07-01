def Reverse(n):
    palindrome = n
    Rev = 0
    while(n > 0):
        digit = n % 10      
        Rev = Rev * 10 + digit  
        n = n // 10
    if(palindrome == Rev):
        print("number is palindrome")
    else:
        print("number is not palindrome")

def main():
    n=int(input("enter number:"))
    Reverse(n)

if __name__ == "__main__":
    main()
            
    
