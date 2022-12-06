# Graphic-Metadata-Tool
A tool for revealing embedded EXIF data in graphic objects and file revision.
<br>

The following document outlines the process that users must follow to effectively use this tool in order to improve archival practice relating to graphic objects. 
<br>
<br>

## Assumptions
- This tool requires the use of command line / terminal functionality
- The directions assume that the user is using MacOS
- The tool is primarily designed for .jpg objects. Additional file formats may be added at a later date.
<br>
<br>
<br>

## Install requisite libraries
In order to use this tool, a number of libraries must be installed on the local device
1. &nbsp; Python3 : https://www.python.org/downloads/
1. &nbsp; Pillow / PIL : https://pillow.readthedocs.io/en/stable/installation.html
  <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; >&nbsp;&nbsp; ```pip install --upgrade pip```
  <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; >&nbsp;&nbsp; ```pip install --upgrade Pillow``` 
1. &nbsp; Piexif : https://pypi.org/project/piexif/
  <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; >&nbsp;&nbsp; ```pip install piexif```
<br>
<br>
<br>

## Use of Tool
1. &nbsp; Download this tool by clicking the green "<> code" icon, selecting "Download zip", and unzip 
1. &nbsp; Open Terminal
1. &nbsp; Specify directory that you wish to work within
<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; >&nbsp;&nbsp; ```cd desktop``` *(example)*
<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Note: The target object and Tool.py need to be located within the specified directory
1. &nbsp; Initiate Python & Tool script
<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; >&nbsp;&nbsp; ```python3 Tool.py```
1. &nbsp; The application will launch within terminal and prompt users to enter a file name
<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Note: When entering the file name, include the extension *(eg example.jpg)*
1. &nbsp; A menu will populate

| Menu Option | Use |
|:---:|:---|
| Print Current Metadata | The embedded metadata associated with the designated graphic object will be printed in a list. <br> The list will appear as element : Value pairs |
| Rename | Users can specify a metadata element to be appended to the end of the current file name. <br> Note: Take care to enter the name of the target element exactly as printed in the list. |
| Edit Metadata | In the event that the embedded metadata needs to be corrected or augmented, this option allows users to adjust the metadata associated with the object. Note: when user is asked to name the new (adjusted) file, make sure to add the file extension. |
| Exit | When the user has finished with the target object, selecting this option will close out of the program and result in the production of a .txt file documenting all of the choices made in relation to the object. <br> Note: This .txt file will share a file name with its associated graphic object and will be saved in the same directory. |

7. &nbsp; Users progress through the application by typing the menu option number located within the brackets
<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp; ex.```[1]``` 
1. &nbsp; It's advised that users proceed sequentially through the menu choices, but it isn't required
1. &nbsp; When finished, select option ```[4]``` to exit the program
1. &nbsp; For work with additional objects, repeat.
<br>
<br>
<br> Important Note: This program is designed to aid in archival processes relating to graphic objects and because of this takes care to do so transparently. Initiating the program and selecting a target file will result in an auditable .txt file documenting all choices made in relation to the selected object. This file should be kept with its correlated object in order to make transparent all actions taken on the object.
<br>
<br>
<br>

## Resources
1. &nbsp; Script to extract Image metadata using Python and Pillow library, https://medium.com/nerd-for-tech/script-to-extract-image-metadata-using-python-and-pillow-library-53a6ae56ccc3
2. &nbsp; Getting today's date in YYYY-MM-DD in Python, https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python
3. &nbsp; Rename Files in Python, https://pynative.com/python-rename-file/#:~:text=Use%20rename()%20method%20of%20an%20OS%20module&text=rename()%20method%20to%20rename,function%20to%20rename%20a%20file
4. &nbsp; Piexif, https://github.com/hMatoba/Piexif
