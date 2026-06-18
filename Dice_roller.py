# roll one or two dices, visual output, track it how many times 
import random

def visual(num) :
    if num == 1:
        print(" +---------+ \n |         | \n |    *    | \n |         | \n +---------+")
    elif num == 2:
        print(" +---------+ \n |       * | \n |         | \n | *       | \n +---------+")
    elif num == 3:
        print(" +---------+ \n |       * | \n |    *    | \n | *       | \n +---------+")
    elif num == 4:
        print(" +---------+ \n | *     * | \n |         | \n | *     * | \n +---------+")
    elif num == 5: 
        print(" +---------+ \n | *     * | \n |    *    | \n | *     * | \n +---------+")
    else:
        print(" +---------+ \n | *  *  * | \n |         | \n | *  *  * | \n +---------+")
        
while True:
    choice = int(input("enter no of dice to roll (1 or 2) : "))
    
    if choice in [1,2] :
        break
    else:
        print("please enter 1 or 2 : ")
        
ct = 0

while True:
    s = input("do you want to roll dice (yes/no) : ").lower()
    
    if s in ["no", "n"] :
        print("rolling stopped!")
        print(f"you rolled dice {ct} times")
        if choice == 2:
            print(f"you rolled both dice {ct} times")
        break;
        
    elif s in ["yes", "y"] :
        roll = random.randint(1,6)
        ct += 1
        print(f"dice rolled : {roll}")
        visual(roll)
        
    else:
        print("please enter yes/no")
        
    if choice == 2 :
        if s in ["yes", "y"] :
            roll2 = random.randint(1,6)
            print(f"dice2 rolled : {roll2}")
            visual(roll2)
            
        else :
            continue