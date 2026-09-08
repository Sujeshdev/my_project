import random as ran
print("GUESS THE NUMBER")
print("RULES ARE:\n1.You have limited atment guess\n2.If youer guess is correct you got 1 point every time\n3.When you can't find number in as er attement your game wil over")
print("\nALL THE BEST\n")
print("Play ---> 1")
print("High Score --> 2")
print("Exit ---> 3")

while True:
    try:
        choice = int(input("Choice your option:"))
        if choice == 1:
            ran_num = ran.randint(1,100)
            score = 0
            ind = 0
            while ind <= 10:
                if ind == 10:
                    print("GAME OVER")
                    print("The number",ran_num)
                    print("your score is:",score)
                    with open("randomgame.txt","a") as f:
                        f.write(f"Score:{score}\n")
                    print("\n")
                    print("Play ---> 1")
                    print("High Score --> 2")
                    print("Exit ---> 3")
                    # print("\n")
                    break
                try:
                    num = int(input("Enter your number(quit game enter 0):"))                    
                    
                    if num == ran_num:
                        print("congratulation you find it")
                        score += 1
                        ind = 0
                        ran_num = ran.randint(1,100)
                        # print(ran_num)

                    elif num == 0:
                         ind = 10

                    elif num > ran_num:
                            print("To big")
                            ind += 1

                    else:
                            print("To small")
                            ind += 1

                except:
                     print("enter number")            
        elif choice == 2:
            score = []
            with open("randomgame.txt","r") as f:
                for line in f:
                    key,val = line.split(":")
                    val = int(val.strip())
                    score.append(val)
                print("your maximum score is",max(score))
                print("\n")
                print("Play ---> 1")
                print("High Score --> 2")
                print("Exit ---> 3")

                
        else:
            print("Thank for palying")
            break
    except:
         print("Enter any choice")
