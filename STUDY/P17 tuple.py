# tuple = coollections which is ordered and unchangeable used to group together related data

student = ("Daniel",21,"male")

print(student.count("Daniel"))
print(student.index(21))

for x in student:
    print(x)

if "Daniel" in student:
    print("Daniel is here mf!")

#The key difference between the tuples and lists is that while the tuples
# are immutable objects the lists are mutable.
# This means that tuples cannot be changed while the lists can be modified.
# Tuples are more memory efficient than the lists.


#----------------CODEWARS--------------
#Write a function called checkCoupon which verifies that a coupon code is valid and not expired.
#A coupon is no more valid on the day AFTER the expiration date. All dates will be passed as strings in this format: "MONTH DATE, YEAR".

from datetime import datetime as dt
def check_coupon(entered_code, correct_code, current_date, expiration_date):
    current, expire = dt.strptime(current_date, '%B %d, %Y'), dt.strptime(expiration_date, '%B %d, %Y')
    if entered_code in correct_code and expire >= current:
        if correct_code == False:
            return False
        else:
            return True
    else:
        return False

print(check_coupon("123", "123", "July 9, 2015", "July 9, 2015"))