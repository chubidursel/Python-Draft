import os
#file detection

path = "C:\\Users\\User\\PycharmProjects\\pythonProject\\test.txt" #don't forget //

if os.path.exists(path):
    print('That location exists!')
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesnt exist")
