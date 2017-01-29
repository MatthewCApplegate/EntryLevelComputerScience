room=0
health=100

fight="You have chosen to fight the man. You must answer a question correctly to beat the man. "

question1="What is the capital of England? "
room1answer="london"

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
           
                
               

    
