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
            random_number = ran.randint(1,100)
            score = 0
            round = 0
            while round <= 10:
                if round == 10:
                    print("GAME OVER")
                    print("The number",random_number)
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
                    user_number = int(input("Enter your number(quit game enter 0):"))                    
                    
                    if user_number == random_number:
                        print("congratulation you find it")
                        score += 1
                        round = 0
                        random_number = ran.randint(1,100)

                    elif user_number == 0:
                         round = 10

                    elif user_number > random_number:
                            print("To big")
                            round += 1

                    else:
                            print("To small")
                            round += 1

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
