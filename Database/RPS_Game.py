import random

user_score = 0
bot_score = 0

user_name = str(input("Enter user name:"))

while True:
    try:
        val = ["rock","paper","scissor","rock","paper","scissor"]
        bot_choice =random.choice(val)

        user_input = str(input("Choice one(Rock,Paper,Scissor),(for quit enter 0):"))
        user_input.islower()

        if user_input == "0":
            break

        if user_input == "rock":
            if bot_choice == "paper":
                print("Bot win")
                bot_score += 1
            elif bot_choice == "scissor":
                print("You won")
                user_score += 1
            else:
                print("Both are same")

        elif user_input == "paper":
            if bot_choice == "scissor":
                print("Bot win")
                bot_score += 1
            elif bot_choice == "rock":
                print("You won")
                user_score += 1
            else:
                print("Both are same")

        elif user_input == "scissor":
            if bot_choice == "paper":
                print("You win")
                user_score += 1
            elif bot_choice == "rock":
                print("Bot won")
                bot_score += 1
            else:
                print("Both are same")
        else:
            print("check spelling")
       
    except:
        print("choice any one(check spelling)")

with open("RPSgame.txt","a") as f:
    f.write(f"User name:{user_name},User score:{user_score},Bot svore:{bot_score}\n")
    if f"{user_score}" > f"{bot_score}":
        f.write(f"{user_name} won the game\n")
    else:
        f.write("Bot won the game\n")

if user_score == bot_score:
    print("The match is tie")
    print("Your score:",user_score,"Bot score:",bot_score)

elif user_score > bot_score:
    print("You beat the bot")
    print("Your score:",user_score,"Bot score:",bot_score)
else:
    print("Bot won the match")
    print("Your score:",user_score,"Bot score:",bot_score)

