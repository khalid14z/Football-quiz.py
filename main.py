print("Welcome to this quiz")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()
print("Okay,Lets get started!!")
score = 0

answer = input("Which country has won the most FIFA World Cup titles?")
if answer == "Brazil":
    print("Well done,That is correct!")
    score += 1
else:
    print("incorrect")
    
answer = input("Which stadium is known as the Theatre of Dreams?")
if answer == "Old Trafford":
    print("Well done,That is correct!")
    score += 1
else:
    print("incorrect")
    
answer = input("Which country hosted the 2018 FIFA World Cup?")
if answer == "Russia":
    print("Well done,That is correct!")
    score += 1
else:
    print("incorrect")
    
answer = input("Who won the UEFA Champions League in the 2020-2021 season?")
if answer == "Chelsea":
    print("Well done,That is correct!")
    score += 1
else:
    print("incorrect")
    
answer = input("Which club is famous for having the invincible season?")
if answer == "Arsenal":
    print("Well done,That is correct!")
    score += 1
else:
    print("incorrect")
    
answer = input("Which country won the Copa America in 2021?")
if answer == "Argentina":
    print("Well done,That is correct!")
    score += 1
else:
    print("incorrect")
    
print("You got " + str(score) +  "questions correct!")
print("You got " + str((score / 6) * 100) +  "%.")
