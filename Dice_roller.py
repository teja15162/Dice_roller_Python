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
        
count = []    
while True:
    ans = input("do you want to roll the dice (yes/no): ").lower()
    
    if ans in ["no","n"] :
        print("dice rolling stopped!")
        if len(count) == 0:
            print("no dice rolled!")
        for i in range(len(count)):
            print(f"dice {i+1} rolled : {count[i]} times")
        break
    
    elif ans in ["yes","y"] :
        try :
            choice = int(input("enter no of dice to roll : "))
        except ValueError:
            print("please enter a number!")
            continue
        
        if choice <= 0:
            print("please enter a positive number")
            continue
        
        for i in range(choice):
            if i < len(count):
                count[i] += 1
            else:
                count.append(1)
                
            roll = random.randint(1,6)
            print(f"dice {i+1} rolled : {roll}")
            visual(roll)
    else :
        print("please enter yes/no : ")
        