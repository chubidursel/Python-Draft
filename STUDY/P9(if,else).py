# if statemet = a block of code that will execute if its condition is true

age = int(input("How old are you?: "))

if age == 100:
    print('You are a century old buddy!') #==  comparison operator for equality
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You haven't been born yet lol")
else:
    print('Are you a child?')

