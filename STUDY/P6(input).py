#input function allows us to write in a console window
name = input("What is your name?: ")
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))

print('Fck off '+name)
print("You  age "+str(age)+" years old") #to display the int (number) put the str beffore age
print("You are "+str(height)+"cm tall")

print("Hello, {} how are you doing today?".format(name))
#f'Hello, {name} how are you doing today?'