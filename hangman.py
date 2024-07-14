

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
import random
new=[]
c=0;e=0
print(logo)
l3 = ["Apple", "Orange", "Banana", "Grape", "Mango", "Pineapple", "Watermelon", "Strawberry", "Cherry", "Pear", "Plum", "Kiwi", "Lemon", "Lime", "Blueberry", "Raspberry", "Blackberry", "Papaya", "Apricot", "Fig"]

x=l3[random.randint(0,len(l3)-1)].lower()
for i in range(len(x)):
    new.append("_")
print(new)
while c!=len(x):
    c2=0
    ch = input("Choose a letter")
    for i in range(len(x)):
        if ch == x[i]:
            new[i] = ch
            c = c + 1
            c2=c2+1
    if c2==0:
        e=e+1
        print(stages[-(e)])
    if e == 7:
        print("You lost The word is ",x)
        break
    print(new)


if c==len(x):
    print("CONGRATULATIONS!!You won")
