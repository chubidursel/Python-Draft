#While loop = a statement that will execute it's block of a code,
#               as long as its condition remains true
#while 1==1:
   # print("Help! I am stuck in a loop!")

name = ""
while len(name) == 0: #till the lenght of my name = 0 keep on printing this prompt
    name = input("Enter your name: ")

print("Hello "+name)

nickname = None#differnt way to code
while not nickname:
    nickname = input("Write your nickname bitch!: ")

print("Hi "+nickname)



# the condition for while will be True as long as the counter variable (count) is less than 3.
count = 0
while (count < 3):
    count = count + 1
    print("Shalom!")


#Python while loop with user input
a = int(input('Enter a number (-1 to quit): '))
while a != -1:
    a = int(input('Enter a number (-1 to quit): '))