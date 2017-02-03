room=0 
health=100

opponent = ["man","knight","king"]

description=[
    "You enter the courtyard and look around. You are surrounded by a \nhigh wall and there is a door at the end of the yard. A man guards the door.",
    "You enter a grand hall and there are small windows along the hall \nand a door at the end guarded by a knight.",
    "You enter a throne room with stained glass windows on either side \nand a chest at the end guarded by the king who is holding the key."]

question = ["What is the capital of England? ", "What is 4+4? ","If king is to queen, lock is to? "]
roomanswer = ["london" ,"8","key"]


player = raw_input("Hello player! Please enter your Character name: ") 
print("Welcome "+player+"! ")  
 
while (True): 
 
    while (room<len(question)): 
        print ("You have "+str(health)+ " health.") 
        print("") 
        print (description[room]) 
        action = raw_input("Press 'F' to fight or 'S' to try and sneak around. ") 
        if (action=="f" or action=="F"):
            answer=raw_input("You have chosen to fight the "+opponent[room]+". You must answer a question \ncorrectly to beat the man. " +"\n\n"+question[room]) 
            if (answer==roomanswer[room]): 
                print("You have beat the "+opponent[room]+" in a fight") 
                room+=1 
            elif (answer!=roomanswer[room]): 
                health-=20 
                print("You try to fight the "+opponent[room]+" but he is too strong") 

        if (action=="s" or action=="S"):
            health-=40
            room+=1

        if (health<0): 
            print("\nYou have failed in your quest and have lost all of your health") 
            room=5
            
    while (room==len(question)): 
        print("") 
        print ("Well done "+player+"! You have successfully rescued the treasure \nwith "+ str(health)+" reamining health.") 
        room=999 
