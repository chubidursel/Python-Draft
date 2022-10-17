#writing files

text = 'Yoooooo! How s going?\nThis is some test\n' # \n means new line
with open('C:\\Users\\User\\PycharmProjects\\pythonProject\\test.txt', "w") as file:
    file.write(text)
print("Done!\nCheck it out!")

#append some text to previous file
text1 = "!!!!New line bitch!"
with open('C:\\Users\\User\\PycharmProjects\\pythonProject\\test.txt', "a") as file: # "a" mode append
    file.write(text1)
print('finished second request!')