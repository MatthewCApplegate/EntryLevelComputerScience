room=0
health=100

fight="You have chosen to fight the man. You must answer a question correctly to beat the man. "

question1="What is the capital of England? "
room1answer="london"

question2="What is 4+4? "
room2answer="8"

question3="If king is to queen, lock is to? "
room3answer="key"

while (True):

    while (room==0):
        player = raw_input("Hello player! Please enter your Character name: ")
        print("Welcome "+player+"! ")
        room=1
        
    
    while (room==1):
        print ("You have "+str(health)+ " health.")
        print("")
        print ("You enter the courtyard and look around. You are surrounded by a high wall and there is a door at the end of the yard. A man guards the door.")
        action = raw_input("Press 'F' to fight or 'S' to try and sneak around. ")
        if (action=="f" or action=="F"):
            answer1=raw_input(fight+question1)
            if (answer1==room1answer):
                print("You have beat the man in a fight")
                room=2
            if (answer1!=room1answer):
                health-=20
                print("You try to fight the man but he is too strong")
                if (health==0):
                    print("You have failed in your quest and have lost all of your health")
                    room=5                
                
    while (room==2):
        print ("You have "+str(health)+ " health.")
        print("")
        print ("You enter a grand hall and look around. There are small windows along the hall and a door at the end guarded by another man.")
        action = raw_input("Press 'F' to fight or 'S' to try and sneak around. ")
        if (action=="f" or action=="F"):
            if (action=="f" or action=="F"):
                answer2=raw_input(fight+question2)
                if (answer2==room2answer):
                    print("You have beat the man in a fight")
                    room=3
                if (answer2!=room2answer):
                    health-=20
                    print("You try to fight the man but he is too strong")
                    if (health==0):
                        print("You have failed in your quest and have lost all of your health")
                        room=5                    

    while (room==3):
        print ("You have "+str(health)+ " health.")
        print("")
        print ("You enter a throne and look around. There are large stained glass windows on either side and a chest at the end guarded by the king who is holding the key.")
        action = raw_input("Press 'F' to fight or 'S' to try and sneak around. ")
        if (action=="f" or action=="F"):
            if (action=="f" or action=="F"):
                answer3=raw_input(fight+question3)
                if (answer3==room3answer):
                    print("You have beat the king in a fight")
                    room=4
                if (answer3!=room3answer):
                    health-=20
                    print("You try to fight the king but he is too strong")
                    if (health==0):
                        print("You have failed in your quest and have lost all of your health")
                        room=5

    while (room==4):
        print("")
        print ("Well done "+"! You have successfully rescued the treasure with "+ str(health)+" reamining health.")
        room=5

    
