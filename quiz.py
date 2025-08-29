

print("Welcome to my computer quiz")
playing = input("Do you want to play? ")
if(playing.lower() != "yes"):
    quit()
print("OKay let's play :)")
score =0
answer= input("what does CPU stand for? ")
if(answer =="central processing unit"):
    print("correct")
    score+=1
else:
    print("incorrect")
answer= input("what is ram? ")
if(answer =="random access memory"):
    print("correct")
    score+=1
else:
    print("incorrect")
answer= input("what does gpu? ")
if(answer =="graphical processing unit"):
    print("correct")
    score+=1
else:
    print("incorrect")
answer= input("what does os? ")
if(answer =="operating system"):
    print("correct")
    score+=1
else:
    print("incorrect") 
print(f"your score is {(score)/4*100} percent")
