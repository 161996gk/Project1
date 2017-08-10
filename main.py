print "Let's get started!"
spy_name = raw_input("Provide your name here : ")
if len(spy_name) > 0 :
    print "Alright "+ spy_name + " i'd like to know more about you before proceeding further. "
    spy_salutation = raw_input("Provide your salutation whether Mr. or Ms. : ")
    spy_name = spy_salutation + "." + spy_name  # the old value get's overwritten here in spy_name
    print "Welcome " + spy_name + ".Glad to have you back here "

# Now inputting of the spy age.
    spy_age = int(raw_input("Provide your age please : "))
  #  print type(spy_age)     #type returns the datatype of the variable.
    if spy_age > 12 and spy_age < 60:
        print "You are eligible for being a Spy."
        # Now check for the Spy rating.

        spy_rating = float(raw_input("Provide the spy rating : "))
        if spy_rating <= 5.0 and spy_rating > 4.7:
            print "The Spy is doing an Excellent job. Keep it up. Proud to have you on board."
        elif spy_rating < 4.7 and spy_rating > 3.7:
            print "The Spy is doing a Good job. Try to enhance your work."
        elif spy_rating < 3.7 and spy_rating > 2.5:
            print "The Spy is doing an Average job. Work a little harder."
        else:
            print "The Spy is not doing a good job. Please work very very Hard."
        #Now check the online info of the spy.
        spy_online = bool(raw_input("Tell whether the spy is Online or not : "))

    else:
        print "Sorry!! You are not eligible for being a Spy. "

else:
    print "Name cannot be empty. Re-enter your name please."


