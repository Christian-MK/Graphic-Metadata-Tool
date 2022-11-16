#Python Group Project
#Christian Koch & Kelso Dunman
#Using Pillow to extract
#https://medium.com/nerd-for-tech/script-to-extract-image-metadata-using-python-and-pillow-library-53a6ae56ccc3


# Photo metadata is a set of data describing and providing information about rights and administration of an image.

import os
from PIL import Image
# Importing Pillow Python Imaging Library:that adds support for opening, manipulating, and saving many different image file formats.
from PIL.ExifTags import TAGS
#script = GroupProject_V1.py    #tied to line print function

from datetime import date       #https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python
from datetime import datetime
today = str(date.today())
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
#Adds current date and time for auditability 
print('======================================================================')
print('\n  Welcome to the Image Archival tool developed by Christian & Kelso.')
while True:
    print('\n======================================================================')
    print('  Please make a selection')
    print('----------------------------------------------------------------------')
    print('\n    [1] Print Metadata')
    print('    [2] Rename')
    print('    [3] Edit Metadata')
#    print('    [5] Print Audit')    #script that prints in terminal activity? Would document all changes/choices regarding object
    print('    [4] Exit')
    print('\n----------------------------------------------------------------------')
    choice = input('Choice: ')

    # Don't ask for image if exiting
    if choice != '4':
        # Select file
        image_file = input('  Enter File Name:\n    ')
        print("----------------------------------------------------------------------")
        
        # Get metadata and store in exif variable
        try:
            image = Image.open(image_file)
        except:
            print('  Invalid Entry.')
            print('    Please Restart.')
            quit()

        # dictionary to store metadata keys and value pairs.
        exif = {}
        # iterating over the dictionary
        for tag, value in image._getexif().items():
        #extarcting all the metadata as key and value pairs and converting them from numerical value to string values
            if tag in TAGS:
                exif[TAGS[tag]] = value

##TODO: Add option to change image

    if choice == '1':
        #checking if image is copyrighted
        try:
            if 'Copyright' in exif:
                print("Image is Copyrighted, by ", exif['Copyright'])
        except KeyError:
            pass

        print()
        print("Displaying all embedded metadata of object: \n")
        for metadata in exif:
            print(metadata + ": " + str(exif[metadata]))
        pass

    # TODO: Check to see if we want to limit which pieces of metadata can be appended to a file rename - need to strip whitespaces and colons
    elif choice == '2':#Rename
        while True:
            old_name = os.path.abspath(image_file)   #we assigned in 1
            while True:
                metadata = input('  Metadata name: \n    ') 
                if metadata not in list(exif.keys()):
                    print(metadata + " is not a metadata")
                    print(list(exif.keys()))
                else:
                    break
            
            val = exif[metadata]
            # TODO: Replace punctuation and white space with dot or underscore
            originalName, fileExtension = os.path.splitext(old_name)

            new_name = originalName + "_" + metadata + "_" + str(val) + fileExtension 
            image.close()
            os.rename(old_name, new_name)
            print(new_name)
            print("  File renamed!")
            
            continue_rename = input('  Continue Renaming? (T/F) \n    ') 
            # TODO: Check they put T or F

            if continue_rename == "F":
                break
            else:
                image_file = new_name
        pass

    elif choice == '3':#Edit Metadata
        print('  This functionality has not yet been released. Stay tuned :)')
        pass

    #elif choice == '5': #prints audit
        #script > out.txt     #https://stackoverflow.com/questions/23364096/how-to-write-output-of-terminal-to-file

    elif choice == '4':#Exit
        print('  Toodles')
        print('======================================================================')
        exit()

    else:
        print('  Sorry, that was an invalid option!')
#        quit()
        pass
