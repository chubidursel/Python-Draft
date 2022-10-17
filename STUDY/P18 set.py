# set = collection which is unordered, unindexed.
#set is faster than a list

utensils = {"fork","spoon","knife","knife"} #No dublicate values
dishes = {"bowl",'plate','cup',"knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()

#dinner_table = utensils.union(dishes) #mix sets
#utensils.update(dishes)
#for x in dinner_table:
 #   print(x)
print(utensils.difference(dishes))
print(utensils.intersection(dishes)) #both sets have in common
