import random
from time import sleep

import requests
from bs4 import BeautifulSoup
import json
import csv

#get HTML file for our URL and save the file

# REQUESTS HTTML file
url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

#  HTTP headers let the client and the server pass additional information with an HTTP request or response.
# *Here we show to website that we aren't bot (not necessary)
headers = {
    "accept" : "*/*",
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
}
#req = requests.get(url, headers=headers)
#src = req.text

#Let's save the site as json file, "cuz some website dont like when someone parsing them !"
#with open("index.html", 'w', encoding="utf8") as file:
#    file.write(src)


#------CREATE A JSON FILE WITH PARTICULAR INFO------
'''''
with open("index.html", encoding="utf8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

all_categories_dict = {}

#get links for each product
all_products_hrefs = soup.find_all(class_="mzr-tc-group-item-href")
for item in all_products_hrefs:
    #print(item)
    item_text = item.text
    item_href = "https://health-diet.ru" + item.get("href")
    #print(f'{item_text}:{item_href}')

    all_categories_dict[item_text] = item_href #add links and names to dict

# save names and links as json file !!!!
# indent=4 >>> write all code in the collumn (not in 1 line)
# ensure_ascii=False >> helps to works with RUS alpabet
with open('all_categories_dict.json', 'w', encoding="utf8") as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)
'''''

with open('all_categories_dict.json', encoding="utf8") as file:
    all_categories = json.load(file)

iteration_count = int(len(all_categories)) - 1
count = 0
print(f'There are {iteration_count} iterations')
#print(all_categories_dict)
for category_name, category_href in all_categories.items():


    # **** HOW TO REPLACE CHARECTERS: [ , - ] INTO _
    rep = [","," ","-"]
    for item in rep:
        if item in category_name:
            category_name=category_name.replace(item, "_")
            #print(category_name)

    req = requests.get(url=category_href, headers=headers)
    src = req.text

    with open(f"data/{count}_{category_name}.html", "w", encoding="utf8") as file:
         file.write(src)

    # Open and save the file as variable
    with open(f"data/{count}_{category_name}.html", encoding="utf8") as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")

    #check web page the presence pf a table
    alert_block = soup.find(class_='uk-alert-danger') #if this class exist on the page
    if alert_block is not None:
        continue #we just keep going to the next page

    #collect all titles
    table_head = soup.find(class_="mzr-tc-group-table").find('tr').find_all('th')
    #print(table_head)
    product = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbohydrates = table_head[4].text
    #print(carbohydrates)

    #create a table (csv file)
    with open(f"data/{count}_{category_name}.csv", "w", encoding="UTF8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                    product,
                    calories,
                    proteins,
                    fats,
                    carbohydrates
            )
        )

    # collecting products
    products_data = soup.find(class_="mzr-tc-group-table").find('tbody').find_all('tr')
    products_info = []
    for item in products_data:
        product_tds = item.find_all("td")

        title = product_tds[0].find('a').text
        calories = product_tds[1].text
        proteins = product_tds[2].text
        fats = product_tds[3].text
        carbohydrates = product_tds[4].text
        #print(proteins)
        products_info.append(
            {
                "Title": title,
                "Calories": calories,
                "Proteins": proteins,
                "Fats": fats,
                "Carbohydrates": carbohydrates
            }
        )

        #PUT the data in csv file
        with open(f"data/{count}_{category_name}.csv", "a", encoding="UTF8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                        title,
                        calories,
                        proteins,
                        fats,
                        carbohydrates
                )
            )

    with open(f"data/{count}_{category_name}.json", "a", encoding="utf-8") as file:
        json.dump(products_info, file, indent=4, ensure_ascii=False)

    count += 1
    print(f'# Iteration №{count}. {category_name} has been written...')
    iteration_count = iteration_count - 1

    if iteration_count == 0:
        print('work is done!')
        break

    print(f'left: {iteration_count}')
    #sleep(random.randrange(1,2))


