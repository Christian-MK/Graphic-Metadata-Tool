#Python Group Project
#Christian Koch & Kelso Dunman
#Using Pillow to extract
#https://medium.com/nerd-for-tech/script-to-extract-image-metadata-using-python-and-pillow-library-53a6ae56ccc3

#Photo metadata is a set of data describing and providing information about rights and administration of an image.
import os
from datetime import date       #Adds current date for auditability
from datetime import datetime   #Adds current time for auditability
import piexif #Specialized library used to modify metadata: https://pypi.org/project/piexif/
from PIL import Image   #Importing Pillow Python Imaging Library adds support for opening, manipulating, and saving many different image file formats.
from PIL.ExifTags import TAGS

today = str(date.today())
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
#https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python

audit = "" #Empty string to add audit

print('\nDate:', today)
audit += '\nDate:' + today + "\n"
print('\n======================================================================')
audit += '\n======================================================================\n' 
print('\n  Welcome to the Image Archival tool developed by Christian & Kelso.')
audit += '\n  Welcome to the Image Archival tool developed by Christian & Kelso.\n'
image_file = input('  Enter File Name:\n    ')
audit += '  Enter File Name:\n    \n'
audit += image_file + "\n"
print("----------------------------------------------------------------------")
audit += "----------------------------------------------------------------------\n"

try:
    image = Image.open(image_file)  #Prevents errors due to invalid inputs
except:
    print('  Invalid Entry.')
    print('    Please Restart.')
    quit()

exif = {}    #Dictionary to store metadata keys and value pairs.

for tag, value in image._getexif().items():  #Iterating over the dictionary

    if tag in TAGS:
        exif[TAGS[tag]] = value  #Extracting all the metadata as key and value pairs and converting them from numerical value to string values

while True:
    print('\n======================================================================')
    audit += '\n======================================================================\n'
    print('  Please make a selection (' + image_file + ")")
    audit += '  Please make a selection (' + image_file + ")\n"
    print('----------------------------------------------------------------------')
    audit += '---------------------------------------------------------------------\n'
    print('\n    [1] Print Current Metadata')
    audit += '\n    [1] Print Current Metadata\n'
    print('    [2] Rename')
    audit += '    [2] Rename\n'
    print('    [3] Edit Metadata')
    audit += '    [3] Edit Metadata\n'
    print('    [4] Exit')
    audit += '    [4] Exit\n'
    print('\n----------------------------------------------------------------------')
    audit += '\n----------------------------------------------------------------------\n'
    choice = input('Choice: ')
    audit += 'Choice: \n'
    audit += choice + '\n'

    if choice == '1':   #Print existing metadata for image
        try:
            if 'Copyright' in exif:  #Checking if image is copyrighted
                print("Image is Copyrighted, by ", exif['Copyright'])
                audit += "Image is Copyrighted, by " + exif['Copyright'] + "\n"
        except KeyError:
            pass

        print("Displaying all embedded metadata of object:")
        audit += "Displaying all embedded metadata of object:\n" 
        print("  Time Accessed:", current_time)
        audit += "  Time Accessed:" + current_time + "\n"
        print(' \n')
        audit += ' \n'
        for metadata in exif:
            print(metadata + ": " + str(exif[metadata]))    #Formats output into 2 columns for ease of view
            audit += metadata + ": " + str(exif[metadata]) + "\n"
            #Should this be ordered? Alphabetically?
        pass

    elif choice == '2': #Rename image files
        while True:
            old_name = os.path.abspath(image_file)
             #https://pynative.com/python-rename-file/#:~:text=Use%20rename()%20method%20of%20an%20OS%20module&text=rename()%20method%20to%20rename,function%20to%20rename%20a%20file.

            while True:
                metadata = input('  Metadata name: \n    ')
                audit += '  Metadata name: \n    \n'
                audit += metadata + "\n"
                if metadata not in list(exif.keys()):
                    print(metadata + " is not a metadata element")
                    audit += metadata + " is not a metadata element \n"
                    print(list(exif.keys()))
                    audit += str(list(exif.keys())) + "\n"
                else:
                    break

            val = exif[metadata]
            #Edge cases where this wouldn't work - colons and dictionaries
            originalName, fileExtension = os.path.splitext(old_name)

            new_name = originalName + "_" + metadata + "_" + str(val) + fileExtension
            image.close()
            os.rename(old_name, new_name)
            print(new_name)
            print("  File renamed!")
            audit += "  File renamed!\n"

            continue_rename = input('  Continue Renaming? (T/F) \n    ')
            audit += "  Continue Renaming? (T/F) \n    \n"
            audit += continue_rename + "\n"
            if continue_rename != "T" or continue_rename != "t":
                break
            else:
                image_file = new_name
        pass

    elif choice == '3': #Edit metadata 
        tag_name = []
        exif_dict = piexif.load(image_file)
        for ifd in ("0th", "Exif", "GPS", "1st"):
            for tag in exif_dict[ifd]:
                tag_name.append(piexif.TAGS[ifd][tag]["name"])
                #https://github.com/hMatoba/Piexif

        #Ask user for metadata element to change
        while True:
            metadata = input('  Metadata element to change: \n    ')
            audit += '  Metadata element to change: \n    \n'
            audit += metadata + "\n"
            if metadata not in tag_name:
                print(metadata + " is not a metadata element")
                audit += metadata + " is not a metadata element\n"
                print(tag_name)
                audit += str(tag_name) + "\n"
            else:
                break
        
        #Convert to ID and locates which dictionary the tag is in
        for ifd in ("0th", "Exif", "GPS", "1st"):
            for tag in exif_dict[ifd]:
                if piexif.TAGS[ifd][tag]["name"] == metadata: 
                    curr_ifd = ifd
                    curr_tag = tag
                    break
        
        #Ask user for new metadata information
        new_metadata = input('  New metadata info: \n    ')
        audit += '  New metadata info: \n    \n'
        audit += new_metadata + "\n"

        if new_metadata.isdigit():
            new_metadata = int(new_metadata)

        #Change metadata
        exif_dict[curr_ifd][curr_tag] = new_metadata
        exif_bytes = piexif.dump(exif_dict) #Converts dictionary to byte format used by PIL to save to image

        #Ask for new file name
        new_filename = input('  New image file name: \n    ')
        audit += '  New image file name: \n    \n'
        audit += new_filename + '\n'
        image.save(new_filename, exif=exif_bytes) #Save metadata within new file; permission issues with overwriting
        
        #Change image for next for loop iteration
        image_file = new_filename
        image = Image.open(new_filename)
        exif = {}    #Dictionary to store new metadata keys and value pairs

        for tag, value in image._getexif().items():  #Iterating over the dictionary
            if tag in TAGS:
                exif[TAGS[tag]] = value
        pass

    elif choice == '4':#Exit
        print('  Toodles')
        audit += '  Toodles\n'
        print('======================================================================')
        audit += '======================================================================\n'
        #open text file
        audit_filename = now.strftime("%Y%m%d") + "_" + image_file + ".txt"
        text_file = open(audit_filename, "w")
    
        #write string to file
        text_file.write(audit)
        
        #close file
        text_file.close()
        exit()

    else:
        print('  Sorry, that was an invalid option!')
        pass

