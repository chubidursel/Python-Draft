#How to delete files
import os
path = "copy.txt"
try:
    os.remove(path)
    #os.rmdir(path) #if u want to delete the folder
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("U do not permission to delete that")
else:
    print(path+"was deleted")


# !!!! from W3
#import os
#if os.path.exists("demofile.txt"):
#  os.remove("demofile.txt")
#else:
#  print("The file does not exist")



# From Bro Code
# if u want to delete directory (folder) and all filies in it:
#import shutil
#shutil.rmtree(path)