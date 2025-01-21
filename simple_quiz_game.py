print("Welcome in Quiz Game!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay! Let;s Play :")

score =0

answer = input("What does CPU stand for?\n")
if answer.lower()== "centeral processing unit":
    print("Correct!")
    score += 1
else:
    print("incorrect!")
    
answer = input("What does GPU stand for?\n")
if answer.lower()== "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("incorrect!")
    
answer = input("What does RAM stand for?\n")
if answer.lower()== "randam access memory":
    print("Correct!")
    score += 1
else:
    print("incorrect!")
    
answer = input("What does SSD stand for?\n")
if answer.lower()== "solid state drive":
    print("Correct!")
    score += 1
else:
    print("incorrect!")
    
print("you got" + str(score) + "question correct!")

print("you got" + str((score/4)*100)+"%.")
    