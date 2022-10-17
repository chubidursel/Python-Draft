# walrus operator :=
#assignment expression aka walrus operator
#assigns values to variables as part of a larger expression

happy = True
print(happy)

#walrus operator
print(sad := False) #assign a value to a variable


#foods = list()
#while True:
#    food = input("What food do you like?: ")
#    if food == "quit":
#        break
#    foods.append(food)

foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)
