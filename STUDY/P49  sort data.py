# sort () method = used with list
# sort () function = used with iterables (повторяемый)

students = ["Dan", "Max", 'Alex', "Mr. Krabs", "Zalupa"]

students.sort(reverse=True) #sort method of lists can accept keywords arguments (key=) (reverse=True)
for i in students:
    print(i)

sorted_students = sorted(students, reverse=True)    #as a function
for i in sorted_students:
    print(i)

# how to sort [list] of (tuples)

animals = [("Dog", "F", 60),
           ("Cat", "A", 12),
           ("Ur mum", "F", 69),
           ("Cow", "B", 1)]

#grade = lambda grades:grades[1]
age = lambda ages:ages[2]
animals.sort(key=age) #sort them by grades


for i in animals:
    print(i)

#from W3
#The sorted() function returns a sorted list of the specified iterable object.
#Strings are sorted alphabetically, and numbers are sorted numerically.

a = (1, 11, 2)
x = sorted(a)
print(x)

a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a, reverse=True)
print(x)

#sort method
cars = ['Ford', 'BMW', 'Volvo']

cars.sort()
print(cars)