#create a game


import random
comp=random.randint(1,10)
i=1 
for i in range(0,6):
    num=int(input("enter a number\n"))
    if i==5:    
        print("Hard luck, You attempt your  all five chances ,the selected",comp,"is the number") 
    elif num<comp:
        print("sorry, your number is low ,take another try")
    elif num>comp:
        print("sorry, your number is greater than comp ,take another try")

    elif num==comp:
        print("congrates,you are winner in",i,"attempts")
        break
     

