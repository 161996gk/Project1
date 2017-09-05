from globals import friends

def select_friend():
    counter = 1
    #Display All friends
    for friend in friends:
        print str(counter) + ". ",friend.displayDetails()
        counter = counter + 1
    if(counter>1):
        result = int(raw_input("Select from the list : "))
        return result - 1
    else:
        return -1