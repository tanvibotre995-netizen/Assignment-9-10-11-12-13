def Reverse(n):
    Rev = 0
    while(n > 0):
        digit = n % 10      
        Rev = Rev * 10 + digit  
        n = n // 10

    print(Rev)

def main():
    n=int(input("enter number:"))
    Reverse(n)

if __name__ == "__main__":
    main()
            
    

            
    
