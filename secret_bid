import os
yes=1
dict={}
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
while (yes):
    name=input("Enter name:")
    bid=int(input("Enter price:"))

    dict[name]=bid
    ch=input("Are there more bidders? yes|no:")
    if ch=="no":
        print(dict)
        lv=list(dict.values())
        name=list(dict.keys())[lv.index(max(lv))]
        print(f"The highest bidder is '{name}' who bid ${max(lv)}")


        yes=0
    elif ch=="yes":
        yes=1
        clear_screen()
    else:
        print("Wrong choise entered")
        yes=0

