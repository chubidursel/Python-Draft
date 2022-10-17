#reading file

with open('C:\\Users\\User\\PycharmProjects\\pythonProject\\test.txt') as file:
    print(file.read())
#print(file.closed)

#if u have any mistake in path or name of the file
try:
    with open('C:\\Users\\User\\PycharmProjects\\pythonProject\\test.tx') as file:
        print(file.read())
except FileNotFoundError:
    print('2nd block of code, That file was not found =(')

