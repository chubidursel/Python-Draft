#slicing - create a substring by extracting elements from another string
#slice our string
#           indexing[] or slice()
#           [start:stop:step]

name = "Dan Bro" #variable that contains our string (Dan Bro)

first_name = name[:3] #computer star with 0 which is the 1st charecter
last_name = name[4:] #or i can code [o:4]
fanky_name = name[0:8:2] #print every 2nd charecters [0:8:2]#phyton assumes that u start wuth 0 charester and stop with the last one
reversed_name = name[::-1] #how to reverse a string


print(first_name)
print(last_name)
print(fanky_name)
print(reversed_name)
print(" ")

website = 'http://google.com'
website1 = 'http://wikipedia.com'

slice = slice(7,-4) #use positive and negative index at the same time

print(website[slice])
print(website1[slice])

# -------------CODEWAR-----------

#Remove anchor from URL
def remove_url_anchor(url):
    return url[:url.find("#")] if "#" in url else url
    #return url.split('#')[0]

url = "www.codewars.com#about"
print(remove_url_anchor(url))