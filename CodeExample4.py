room=0
health=100

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
          
                
       



    
