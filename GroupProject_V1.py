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
print('======================================================================')
print('\n  Welcome to the Image Archival tool developed by Christian & Kelso.')
while True:
    print('\n======================================================================')
    print('  Please make a selection')
    print('----------------------------------------------------------------------')
    print('\n    [1] New File')
    print('    [2] Rename')
    print('    [3] Edit Metadata')
#    print('    [5] Print Audit')    #script that prints in terminal activity? Would document all changes/choices regarding object
    print('    [4] Exit')
    print('\n----------------------------------------------------------------------')
    choice = input('Choice: ')

    if choice == '1':
        image_file = input('  Enter File Name:\n    ')
        print("----------------------------------------------------------------------")
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

        #checking if image is copyrighted
        try:
            if 'Copyright' in exif:
                print("Image is Copyrighted, by ", exif['Copyright'])
        except KeyError:
            pass

        print()
        print("Displaying all embedded metadata of object: \n")
        print(exif)
        pass

    elif choice == '2':#Rename
    #https://pynative.com/python-rename-file/#:~:text=Use%20rename()%20method%20of%20an%20OS%20module&text=rename()%20method%20to%20rename,function%20to%20rename%20a%20file.
        old_name = os.path.abspath(image_file)   #we assigned in 1
        print(old_name)
        #disect
        #x = old_name
        #y = re.findall(^image_file (\S+).jpg, x)
        #print(y)
        #reconstitute
        new_name = old_name +str(3) #+ str('.jpg') #works. need to write a way to find the last "." and write to the left. or delete .jpg and add after
        print(new_name)     #'new_details.txt'
        #there should be a way to append dictionary key:values to the absolute path/name
        os.rename(old_name, new_name)
        print("  File renamed!")
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
