# exception = events detected during execution that interrupt the flow of a programm.

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
    print(result)
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! Idiot))")
except ValueError:
    print("Enter only numbers plz")
except Exception:
    print("something went wrong =(")
#else:
#    print(result)
finally: #always execute
    print("This will always execute")

#           from W3

#The (try) block lets you test a block of code for errors.
#The except block lets you handle the error.
#The else block lets you execute code when there is no error.
#The finally block lets you execute code, regardless of the result of the try- and except blocks.

x = "The code from W3"
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")