# copyfile() = copy contents of a file
#copy() = copyfile() + permission mode + destination can be a directory
#copy2 = copy() +copy metadata (file's creation and modification time)

import shutil

shutil.copyfile('test1.txt', 'copy.txt') # make a copy in a same folder
shutil.copy('test1.txt', 'C:\\Users\\User\\PycharmProjects\\pythonProject\\copy1.txt')
