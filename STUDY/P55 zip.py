#  zip (*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
# create a zip object with paired stored in tuples for each element
#aka Parallel Iteration

usernames = ["Dan_21", "baurim", "FFF-21"]
passwords = ("qwerty1","lololol", "0000 the most seciure")
login_date = ["1.2.1996", "24.2.2022", "8.3.2022"]

users = zip(usernames, passwords, login_date)

print(type(users))

for i in users:
    print(i)


#from W3
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = dict(zip(a, b)) #drint as dict-type
print(type(x))

for key, value in x.items(): #need key and value
    print(key, value)