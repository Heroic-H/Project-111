import os
import shutil
from_dir="C:/Users/batul/Downloads"
to_dir="C:/Users/batul/OneDrive/Desktop/My Stuff/Heroic H/Coding Classes/Homework"
listOfFiles=os.listdir(from_dir)
#print(listOfFiles)
for fileName in listOfFiles:
    name,extension=os.path.splitext(fileName)
    print(name)
    print(extension)