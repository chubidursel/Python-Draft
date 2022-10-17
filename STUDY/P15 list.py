# list = used to store multiple items in a single variable
# !!!!! CHECK P53 COMPREHENSION !!!! (there r a lot answers about list)


food = ["pizza","borsh","hotdog","spaghrtti"]

#food[0] = "sushi"

#print(food[0])
food.append("ice cream") #append (добавить)
food.remove("hotdog")
food.pop() #remove the last item in the list
food.insert(0, "cake",) #insert(вставлять) a value at a given index
food.sort() #sort list alphabetically
#food.clear()#remove everything

for x in food:
    print(x)

print(food)

#---------- from codewars (GAME) -------

#Multiplying each element of a list by a number
def multiplyList(myList):
    multiplied_list = [element * 2 for element in myList]
    return multiplied_list
#     return [2 * x for x in myList]

list1 = [1, 2, 3, 4]
print(multiplyList(list1))

#how to sort a list from largest to smallest
list3 = [1,2,3,4,5]
list3.sort(reverse=True)
print(list3)

# get rid of all negative numbers and sum the rest
def positive_sum(arr):
    arr = [item for item in arr if item >= 0] #check P53
    if arr == [""]:
        return 0
    else:
        arr = map(abs, arr)
        return sum(arr)
arr = [-1,2,3,-4,-5]
print(positive_sum(arr))

# --------------check 2 list and add or subtract the points -----------------
def check_exam(arr1,arr2):
    res = 0
    # As len(arr1) = len(arr2) I choose one of them.
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            if arr2[i] != "":
                res -= 1
            else:
                res += 0  # Blank answer.
        elif arr1[i] == arr2[i]:
            res += 4
    return res
arr1 = ['a','a','b','c']
arr2 = ['a','c','b','c']
print(check_exam(arr1,arr2))