# import statements.
from spy_details import spy
from start_chat import start_chat
from globals import Spy
import re

print "Let's get started!!!"
question = "Do you want to continue as " + spy.Name + "(Y/N) ? "
existing = raw_input(question)

# validating users input
if existing.upper() == "Y":
    # default user
    start_chat(spy.Name, spy.Age, spy.Rating, spy.SpyOnline)

elif existing.upper() == "N":
    # new user code here
    wholecheck=True#temporary variable
    while(wholecheck):
        tempcheck=True#temporary variable
        # Validation Using Regex
        patternsalutation='^Mr|Mrs$'
        patternname='^[A-Za-z\s]+$'
        patternage='^[0-9]+$'
        patternrating='^[0-9]+\.[0-9]$'
        # Validating Each Values Using Regular Expression
        while tempcheck:
            salutation = raw_input("Mr. or Ms.? : ")
            if (re.match(patternsalutation, salutation) != None):
                tempcheck = False
            else:
                print "Enter Again!!!!"
        tempcheck=True
        while tempcheck:
            spy.Name=raw_input("Enter Name: ")
            if(re.match(patternname,spy.Name)!=None):
                tempcheck=False
            else:
                print "Enter Again!!!!"

            # concatenation.
            spy.Name = salutation + "."+spy.Name
        tempcheck=True
        while tempcheck:
             spy.Age = raw_input("Age?")
             if (re.match(patternage, spy.Age) != None):
                 tempcheck = False
                 spy.Age=int(spy.Age)
             else:
                 print "Enter Again!!!!"
        tempcheck=True
        while tempcheck:
            spy.Rating = raw_input("Spy rating?")
            if (re.match(patternrating, spy.Rating) != None):
                tempcheck = False
                spy.Rating=float(spy.Rating)
            else:
                print "Enter Again!!!!"
        # Checking If Spy is eligible
        if spy.Rating <= 5.0 and spy.Age > 12 and spy.Age < 60:
            start_chat(spy.Name,spy.Age,spy.Rating,spy.SpyOnline)
            wholecheck=False
        else:
            print "Invalid Entry!!!!Start From Scratch."
else:
    print "Wrong choice. Try again"