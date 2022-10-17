import csv

#basic
'''''
name_1 = "Daniel"
name_2 = "Max"
#or you can pass as the parameter (same)
date_names = ["Mahmud", "Yasha"] 

with open("data2.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(
        #[name_1, name_2]
        date_names
    )
'''''
# part 2
'''''
with open("data2.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(
        ('user_name', 'user_address')
    )
user_data = [
    ["Ben", "Bangkok"],
    ["Bob", "NY"],
    ["Steve", "Kharkiv"],
    ["Lucy", "Tokyo"]
]
for user in user_data:
    with open("data2.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(
            user
        )
print("Finished!")
'''''
# part 2.1 (same same but different)
user_data = [
    ('user_name', 'user_address'),
    ["Ben-Ten", "Bangkok"],
    ["Bob", "NY"],
    ["Steve", "Kharkiv"],
    ["Lucy", "Tokyo"]
]
with open("data2.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows( #writerows <<< S
        user_data
    )
print("Finished! part 2.1")