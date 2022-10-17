#The requests module allows you to send HTTP requests using Python.

import requests

from PIL import Image #Pillow librarary works with pictures
from io import BytesIO #works with bites (ps > convert bites into pictures)

#-----------------download pictures from PEXELS -----------------------------
# https://www.pexels.com/api/documentation/#photos-show

#The GET method indicates that you’re trying to get or retrieve data from a specified resource.
# "status code" = informs you of the status of the request. (.status_code returned a 200, which means your request was successful and the server responded with the data you were requesting.)
#       if response.status_code == 200:
#               print('Success!')
#       elif response.status_code == 404:
#               print('Not Found.')
# To see the response’s content in bytes, you use .content

# **** PARAMS
#to customize a GET request is to pass values through query string parameters in the URL.
# To do this using get(), you pass data to params >>> params = {"query": query, "per_page": 1}

# **** HEADER
# pass a dictionary of HTTP headers to get() using the headers parameter.  header = {"Authorization": "***API KEY***"}
# The Accept header >>> tells the server what content types your application can handle (PERSONAL API key)


#----------------------------------------
# www.httpbin.org >>> website that designed for showing u how ir requesting responses look like from the service
url = 'https://www.httpbin.org/headers'
r = requests.get(url)
print(r.text)
print('----------------------------------------')
#if you have authentication issues >>> use headers

url = 'https://www.httpbin.org/headers'
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
    #'Accept-Language' // 'Accept' ect
}
r = requests.get(url, headers=headers)
print(r.text)
print('----------------------------------------')

def download(query: str, page_count: str):
    header = {"Authorization": "563492ad6f91700001000001202f67cb40e541d9925e5e5f68365d68"}
    params = {"query": query, "per_page": 1}
    url = f"https://api.pexels.com/v1/search"
    i = 1
    while i <= int(page_count):
        params['page'] = i
        r = requests.get(url, headers=header, params=params) #pass parameer though medthod params not like in example below
        #url = f"https://api.pexels.com/v1/search?query={query}&per_page=1&page={i}"

        if r.status_code == 200: #r.status_code >>>> respose from server (200 =good || 404 = bad)
            r1 = r.json()
            for item in r1.get('photos'):
                _img_url = item.get('src').get('original')
                resp = requests.get(_img_url)

                print(_img_url)
                #print(_img_url.split('.')[-1]) #check the format of this file
                #print(resp.content) #bites image
                image = Image.open(BytesIO(resp.content)) #convert from bite into normal picture
                image.save(f"media/{query}_{i}.{_img_url.split('.')[-1]}")
        else:
            print(r.status_code)
        i += 1
def main() -> None:
    query = input("Query: ")
    page_count = input("Page: ")
    download(query, page_count)
main()

print("I am done!!!")

"""
ppp = {"q" : 'Bangkok'}
page = requests.get("https://www.wikipedia.org/", params=ppp)

if page.status_code == 200: # have conection with website
#    print(page.content) #recive HTML file
#    print(page.content.decode("utf-8")) #encoding to Python str
#    print(page.text) #he text encoding guessed by Requests is used when you access .text
    print(page.url)

else:
    print("We ar fucked!", page.status_code)
"""

#--------EXAMPLES------------
"""
 try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data['main']["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:

"""