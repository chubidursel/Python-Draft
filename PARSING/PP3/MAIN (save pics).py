import requests

def get_data():
    # i dint find an accept string (seems like web site doesnt allow to see)
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
    }

    for i in range(1,49):
        url=f"https://www.recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg"
        req = requests.get(url=url, headers=headers)
        response = req.content

        with open(f'media/{i}.jpg',"wb") as file:
            file.write(response)
            print(f"Downloaded {i} of 48")

def main():
    get_data()

if __name__=="__main__":
    main()
