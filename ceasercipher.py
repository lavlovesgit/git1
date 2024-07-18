def cipher(s1,n,ch2):
    s2=""
    if ch2=='decoded':
        n=-1*n
    for i in s1:
        x = ord(i) + n
        s2 = s2 + chr(x)
    print(f"{ch2} string:{s2}")

yes=1
while(yes):
    ch2=input("Enter  'encoded'| ' decoded':")
    s1 = input("Enter string:")
    n = int(input("Secret code:"))
    if ch2=='encoded' or ch2=='decoded':
        cipher(s1, n, ch2)
    else:
        print("Wrong choise")
        yes=0



    ch1=input("Enter 'yes' to continue 'no' to discontinue:")
    if ch1=="yes":
        yes=1
    elif(ch1=="no"):
        yes=0
    else:
        print("Wrong choise.")
        break
