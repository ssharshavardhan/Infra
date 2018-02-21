Problem Statement
Create a program/script in any language like Python, Bash, C, C++ etc. The program should
scan all the Drives and folders like C:/User/* (Windows) and /home/* (Linux) recursively and
then identify the top 10 files which have the largest size on the system.

Example: The tool should scan the Downloads folder, Documents Folder, Movies folder, C drive, E
drive etc and display the 10 biggest files in these folders with their size in MB.
The tool should sort the files on Desktop on the basis of file extension and move them in
separate folders in Documents folder.
Example: If there are 10 MP3 files, 3 word documents, 4 PDFs then in Documents Folder three
folders should be created with name MP3, DOC and PDF and all the files on the Desktop should
be moved into these directories based on their file type or extension. Desktop should be cleaned
but dont remove shortcuts of My Computer, Chrome or even Counter strike.

---------------------------------------------------------------------------------------------------------

##Working
It operates in modes
1. Gets N largest files of system
    *Sort files by least recently used
2. Sort the files on Desktop
    *Sort based on valid extensions
    *Sort based on kinds of extensions
    *List files and folders on your Desktop
    *Sort folders based on data they hold like images etc.
3. List duplicate files on your system    
4. Exit

LIBRARIES USED:
1) os
2) shutil
3) sys
4) platform
5) hashlib 
6) socket
7) call

LANGUAGE USED:
Python 2.7.12

PLATFORMS SUPPORTED:
1) Linux.
2) Windows.
