def Vowel_constant(ch):
    if(ch=='a'or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        print("vowel")
    else:
        print("constant")

def main():
    ch=input("enter a letter:")
    Vowel_constant(ch)

if __name__ == "__main__":
    main()
