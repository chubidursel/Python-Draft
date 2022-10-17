import time
# for loops = a statement that will execute it's blcok of code
#           a limited amount of time
# while loop = unlimeted
# for loop = limited

for i in range(7):
    print(i+1)

for w in range(80,100+1,2): #range(диапазоня)
    print(w)

for i in "Daniel": #iterable (повторяемый)
    print(i)

#from W3

#Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#from betacode (RUS)
#Использование цикла for может помочь вам просматривать на элементах массива.
print("For loop example")
# Объявить массив.
names = ["Tom", "Jerry", "Donald"]

for name in names:
    print("Name = ", name)

print("End of example")