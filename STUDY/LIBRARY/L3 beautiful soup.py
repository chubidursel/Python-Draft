# Beautiful Soup is a Python library for pulling data out of HTML and XML files.

from bs4 import BeautifulSoup

with open("blank/index2.html", encoding="utf8") as file:
    src = file.read()
#print(src) #we can read this file in a console

# Here we have to put HTML file into bs4 structure
soup = BeautifulSoup(src, "lxml") # 1.param>>HMTL file || 2.param>>parser

dock = soup.prettify()
print(dock)

#title = soup.title
#print(title)
#print(title.text)
#print(title.string)

# !!!! method >>> .find() .find_all() !!!!!!!
page_h1 = soup.find("h1")
print(page_h1)

page_h1_all = soup.find_all("h1")
print(page_h1_all)

for item in page_h1_all:
    print(item.text)

user_name = soup.find("div",class_= "user__name")
print(user_name) # << print SOUP object
print(user_name.text)
print(user_name.text.strip()) # clean text

# atribute to find == .find("span").text
#user_name = soup.find(class_="user__name").find("span").text
#print(user_name)

#another atribute to find == dict
#user_name = soup.find("div", {"class": "user__name"}).find("span").text
#print(user_name)

find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")
print(find_all_spans_in_user_info)

for item in find_all_spans_in_user_info:
     print(item.text)

print(find_all_spans_in_user_info[0])
print(find_all_spans_in_user_info[2].text)

# **** HOW TO PARSE LINKS to social media ****
# 1 option (go through blocks and classes to get links)
social_links = soup.find(class_="social__networks").find("ul").find_all("a")
print(social_links)

# 2 option "EASY" (find all tags "a" in this file) BUT! if there s another link with "a" u will get it
#all_a = soup.find_all("a")
#print(all_a)

#----CREATE a for loop to print all links---- || links always kept in atribute href ||
for item in social_links:
    item_text = item.text
    item_url = item.get("href")
    print(f"{item_text}: {item_url}")

print(" **************   FIND PARENT CLASS   *******************")
# .find_parent() .find_parents() <<< (if u want to move UP in code to find smth within parent class >> use this method)

post_div = soup.find(class_="post__text").find_parent()
print(post_div) #so we take block of code till previous parent (<div class ="user_post_info">)

#post_div = soup.find(class_="post__text").find_parent("div", "user__post")
#print(post_div)

# post_div = soup.find(class_="post__text").find_parent()
# print(post_div)

# post_divs = soup.find(class_="post__text").find_parents("div", "user__post")
# print(post_divs)

print("-------------NEXT ELEMENT------------")
# .next_element .previous_element
next_el = soup.find(class_="post__title").next_element.next_element.text
print(next_el)

next_el1 = soup.find(class_="post__title").find_next().text #same method but better i guess
print(next_el1)

# .find_next_sibling() .find_previous_sibling()
next_sib = soup.find(class_="post__title").find_next_sibling()
print(next_sib)


links = soup.find(class_="some__links").find_all("a")
print(links)

for link in links:
    #THere 2 option to parse date (1 .get ||| 2. just with the link )
    link_href_attr = link.get("href")
    link_href_attr1 = link["href"]

    link_data_attr = link.get("data-attr")
    link_data_attr1 = link["data-attr"]
    print(link_href_attr1)
    print(link_data_attr1)

# NONE! We CAN NOT find the link "Одежда для взрослых" if we write only part of that sentence
find_a_by_text = soup.find("a", text="Одежда")
print(find_a_by_text)

find_a_by_text1 = soup.find("a", text="Одежда для взрослых").text
print(find_a_by_text1)

import re
# with library re and method compile >>> can find a link with a PART OF THE PARAMETER!!!

find_a_by_text = soup.find("a", text=re.compile("Одежда"))
print(find_a_by_text)

find_all_clothes = soup.find_all(text=re.compile("([Оо]дежда)"))
print(find_all_clothes)