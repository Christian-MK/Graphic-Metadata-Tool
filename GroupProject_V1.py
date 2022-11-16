#Python Group Project
#Christian Koch & Kelso Dunman
#Using Pillow to extract
#https://medium.com/nerd-for-tech/script-to-extract-image-metadata-using-python-and-pillow-library-53a6ae56ccc3

# Photo metadata is a set of data describing and providing information about rights and administration of an image.

from datetime import date       #Adds current date for auditability
from datetime import datetime   #Adds current time for auditability
today = str(date.today())
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
#https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python

import os
from PIL import Image   # Importing Pillow Python Imaging Library adds support for opening, manipulating, and saving many different image file formats.
from PIL.ExifTags import TAGS
print('\nDate:', today)
print('\n======================================================================')
print('\n  Welcome to the Image Archival tool developed by Christian & Kelso.')
while True:
    print('\n======================================================================')
    print('  Please make a selection')
    print('----------------------------------------------------------------------')
    print('\n    [1] New File: Print Metadata')
    print('    [2] Rename')
    print('    [3] Edit Metadata')
#    print('    [5] Print Audit')    #script that prints in terminal activity? Would document all changes/choices regarding object
#Maybe this shouldnt be an option. Just a product of the system
    print('    [4] Exit')
    print('\n----------------------------------------------------------------------')
    choice = input('Choice: ')

    if choice == '1':   #New File: Print Metadata
        image_file = input('  Enter File Name:\n    ')
        print("----------------------------------------------------------------------")
        try:
            image = Image.open(image_file)  #Prevents errors due to invalid inputs
        except:
            print('  Invalid Entry.')
            print('    Please Restart.')
            quit()

        exif = {}    # dictionary to store metadata keys and value pairs.

        for tag, value in image._getexif().items():  # iterating over the dictionary

            if tag in TAGS:
                exif[TAGS[tag]] = value  #extarcting all the metadata as key and value pairs and converting them from numerical value to string values

        try:
            if 'Copyright' in exif:  #checking if image is copyrighted
                print("Image is Copyrighted, by ", exif['Copyright'])
        except KeyError:
            pass

        print() #   ???whats this for??
        print("Displaying all embedded metadata of object:")
        print("  Time Accessed:", current_time)
        print(' \n')
        for metadata in exif:
            print(metadata + ": " + str(exif[metadata]))    #Formats output into 2 columns for ease of view
            #Should this be ordered? Alphabetically?
        pass

    elif choice == '2':#Rename
        while True:
            old_name = os.path.abspath(image_file)   #we assigned in 1
             #https://pynative.com/python-rename-file/#:~:text=Use%20rename()%20method%20of%20an%20OS%20module&text=rename()%20method%20to%20rename,function%20to%20rename%20a%20file.

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
            if continue_rename != "T" or "t":   #Catches if user tries to use capital or no
                break
            else:
                image_file = new_name
            pass

    elif choice == '3':#Edit Metadata
        print('This functionality has not yet been released. Stay tuned :)')
        pass

    #elif choice == '5': #prints audit
        #script > out.txt     #https://stackoverflow.com/questions/23364096/how-to-write-output-of-terminal-to-file
        #txt file should be created/opened at the point of image open
        #all actions executed on file should be printed to file
        #file closed when choice 1 is selected again
        #txt file must share name with image
        #txt name must change with image during option 2

    elif choice == '4':#Exit
        print('  Toodles')
        print('======================================================================')
        exit()

    else:
        print('  Sorry, that was an invalid option!')
#        quit()
        pass

