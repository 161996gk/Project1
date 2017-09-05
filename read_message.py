from select_friend import select_friend
from globals import friends
from steganography.steganography import Steganography
import re
def read_message():
    #function logic
    friend_choice = select_friend()
    #Checking if Friend List is not empty
    if friend_choice!=(-1):
        pattern='^[A-Za-z][0-9A-Za-z\s]+\.jpg$'
        a=True #temporary variable
        #Average Words
        friends[friend_choice].calcAverageWords()
        #prepare the  message
        while a:
            try:
                output_image = raw_input("Provide the name of the image to be decrypted: ")
                if(re.match(pattern,output_image)!=None):
                    a=False
                else:
                    print "Enter Again!!!!"
            except IOError:
                print "Enter Image Name That Exists!!!!"
        try:
            #Decrypt the message
            text = Steganography.decode(output_image)
            print "Message:",text
        except TypeError:
            #Blank Image Case i.e. No Decrypted Message in Image
            print "Image does not have any message!!!!"
    else:
        print "Empty Friend's List!!!!"