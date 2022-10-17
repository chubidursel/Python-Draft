name = "Daneil"

print(len(name)) #len = lenght (длина)
print(name.find("a")) #where is in our varuable this string (1) cuz computer stars with 0
print(name.capitalize()) #capitalaze our name (starts with a capital letter)
print(name.upper()) # upercase
print(name.lower())
print(name.isdigit()) #numbers will say True
print(name.isalpha()) #to check to see if our string contains only letters
print(name.count("a")) #How many characters are in our str
print(name.replace('a', 'o')) #use to replace one character to another
print(name*3) #we can display str multiple times


# ---------CODEWARS---------
#Use the indexing notation string[index] with index as 0 to get the first character of a string.
def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r": #if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
print(are_you_playing_banjo("rockk"))
# or better code
#return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo";

# NEXT EXERCISE (find how many character are repeated)
def is_isogram(string):
    count = {}
    for s in string:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1

    for key in count:
        if count[key] > 1:
            return False
    else:
        return True
string = "moose"
print(is_isogram(string))

#>>>>>>>>>>>>>>>>>>>next
#In this little assignment you are given a string of space separated numbers,
#and have to return the highest and lowest number.
def high_and_low(numbers):
    numbers = numbers.split() #<<< split str
    numbers = [int(i) for i in numbers]
    return str(max(numbers)) + " " + str(min(numbers))
numbers = ("1 2 3 4 5")
print(high_and_low(numbers))