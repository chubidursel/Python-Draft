# str. format = optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

print("The "+animal+' jump over the '+item)
print('The {} jump over the {}'.format(item, animal)) # {curly braces} = format fields
print('The {1} jump over the {0}'.format(item, animal)) #positional argument

print('The {animal} jump over the {item}'.format(item = "stone", animal = "goat")) #keyword arg
print('The {animal} jump over the {animal}'.format(item = "stone", animal = "cat"))

#more ellegant way =)
text = "The {} jump over the {}"
print(text.format(animal, item))

#add padding to string (добавить отступ к строке)

name = "Daniel"

print("Hello, my name is: {}".format(name))
print("Hello, my name is: {:10}".format(name)) #add padding
print("Hello, my name is: {:10}. Nice to meet you fcker!".format(name))
print("Hello, my name is: {:<10}. Nice to meet you fcker!".format(name)) #left align (выравнивание по левому краю)
print("Hello, my name is: {:>10}. Nice to meet you fcker!".format(name))
print("Hello, my name is: {:^10}. Nice to meet you fcker!".format(name)) #caenter align

number = 3.1415
print("The number pi is {}".format(number))
print("The number pi is {:.2f}".format(number))

number1 = 1000
print("The number there is {:.3f}".format(number1))
print("The number there is {:,}".format(number1))
print("The number there is {:b}".format(number1)) #binary representation of your number
print("The number there is {:o}".format(number1)) #octal number
print("The number there is {:x}".format(number1)) # hexadecimal
print("The number there is {:E}".format(number1)) #scientific notation


print(" ")
#from W3

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
#The format() method formats the specified value(s) and insert them inside the string's placeholder.

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1)
#The placeholders can be identified using
# named indexes {price}, numbered indexes {0}, or even empty placeholders {}.

print(" ")
#           from GG

# the str.format() method
# using format option in a simple string
print("{}, A computer science portal for geeks."
      .format("GeeksforGeeks"))

# using format option for a
# value stored in a variable
str = "This article is written in {}"
print(str.format("Python"))

# formatting a string using a numeric constant
print("Hello, I am {} years old !".format(18))
