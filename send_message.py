from select_friend import select_friend
from steganography.steganography import Steganography
from globals import friends,Chat
from datetime import datetime
import re
def send_message():
    #function logic
    friend_choice = select_friend()
    #checking If Friend's List Is not Empty
    if friend_choice!=-1:
        pattern='^[A-Za-z][0-9A-Za-z\s]+\.jpg$'
        patternsave='^SOS|SAVE ME|IN DANGER|HELP$'
        a=True
        #prepare the  message
        while a:
            original_image = raw_input("Provide the name of the image to hide the message: ")
            if(re.match(pattern,original_image)!=None):
                a=False
            else:
                print "Enter Again!!!!"
        a=True
        while a:
            output_image = raw_input("Provide the name of the output image : ")
            if (re.match(pattern, output_image) != None):
                a = False
        text = raw_input("Enter your message here: ")
        if(len(text)>100):
            print "Large Message Input!!!!"
            print "You are no more a Spy!!!!"
            friends.remove(friends[friend_choice])
        else:
            #Handling Exception If Image Does Not Exist
            try:
                # Encrypt the message
                Steganography.encode(original_image,output_image,text)
                chatobject=Chat(output_image,datetime.now())
                friends[friend_choice].chat.append(chatobject)
                #Successful message
                print "Your message encrpyted successfully"
                # Handling Situation For SOS
                if (re.match(patternsave, text.upper()) != None):
                    print "I got your location!!!!I'll be there soon!"
            except IOError:
                print "Image Does Not Exist!!!!"
    else:
        print "Empty Friend's List!!!!"