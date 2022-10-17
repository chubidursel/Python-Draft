#Loop control Statements = change a loops execution (исполнение) from its normal sequence

# break = used to terminate the loop entirely
#continue = skips to the next interation of the loop.
# pass = soes nothing, act as a placeholder.
while True:
     name = input("Enter your name: ")
     if name != "": # != doesn't equal #"" typein anything
         break
print("Hello " +name)

phone_number = "123-456-789"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

print(' ')

for i in range (1,21):
    if i == 13:
        pass
    else:
        print(i)