# import statements.
from globals import friends,Spy

# add new friends.
import re
def add_friend():
    new_friend =Spy(" "," ",0,0.0,False)
    tempcheck=True#temporary variable
    #Validation Using Regex
    patternsalutation='^Mr|Ms$'
    patternname='^[A-Za-z][A-Za-z\s]+$'
    patternage='^[0-9]+$'
    patternrating='^[0-9]+\.[0-9]$'
    #Validating Each Values Using Regular Expression
    while tempcheck:
        salutation = raw_input("Mr. or Ms.? : ")
        if (re.match(patternsalutation, salutation) != None):
            tempcheck = False
        else:
            print "Enter Again!!!!"
    tempcheck=True
    while tempcheck:
        new_friend.Name=raw_input("Enter Name: ")
        if(re.match(patternname,new_friend.Name)!=None):
            tempcheck=False
        else:
            print "Enter Again!!!!"

    # concatenation.
    new_friend.Name = salutation + "."+new_friend.Name
    tempcheck=True
    while tempcheck:
        new_friend.Age = raw_input("Age?")
        if (re.match(patternage, new_friend.Age) != None):
            tempcheck = False
            new_friend.Age=int(new_friend.Age)
        else:
            print "Enter Again!!!!"
    tempcheck=True #temporary variable
    while tempcheck:
        new_friend.Rating = raw_input("Spy rating?")
        if (re.match(patternrating, new_friend.Rating) != None):
            tempcheck = False
            new_friend.Rating=float(new_friend.Rating)
        else:
            print "Enter Again!!!!"
    # validating input
    if new_friend.Rating <= 5.0 and new_friend.Age > 12 and new_friend.Age < 60:
        # add_friend
        friends.append(new_friend)
        print "Friend Added"
    else:
        print "Sorry invalid entry!!!!"
    # returning number of friends
    return len(friends)