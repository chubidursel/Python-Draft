#list comprehension = a way to create a new list with less syntax
#                      2nd option can mimic certain lambda functions, easier to read
# list = [expression for item in iterable]
# list = [expression for item in iterable if conditional]

squares = []                #create an empty list
for i in range(1,11):       # create a for loop
    squares.append(i*i)     #define what each loop iteration should do
print(squares)

# list comprehension (same thing but less code and easy to read)
# list = [z*z (expresion) for z (item) in range(1,11)(iterable)]
squares_1 = [z * z for z in range(1,11)]
print(squares_1)

#2nd option can mimic certain lambda functions, easier to read

students = [100, 90, 80, 70, 60,40, 33, 21, 0]
passed_students = list(filter(lambda x: x >= 60, students))
print(passed_students)

# same program but with list comprehension
kids = [100, 93, 82, 72, 61, 42, 33, 21, 0]

# list = [expression for item in iterable if conditional]
passed_kids = [i for i in kids if i >=60]

# list = [expression (if/else) for item in iterable if conditional]
passed_kids = [i if i >=60 else "FAILED" for i in kids]
print(passed_kids)


#from W3
#long version
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

#with list comprehension (same thing but less code)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#------------CODEWARS-------
def reverseWordSentence(text):
    words = text.split(" ") # Splitting the Sentence into list of words.
    newWords = [word[::-1] for word in words] # List Comprehension Technique (Reversing each word and creating)
    newSentence = " ".join(newWords) # Joining the new list of words to for a new Sentence

    return newSentence

text = "bike is very clean"
print(reverseWordSentence(text))

#return ' '.join(s[::-1] for s in str.split(' '))
