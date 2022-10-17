import requests

headers = {
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
}

def get_data_file(headers):
    url = 'https://www.landingfolio.com/'
    r = requests.get(url=url, headers=headers)
    with open("index.html", 'w', encoding='utf-8') as file:
        file.write(r.text)

def download_imgs(file_path):
    pass

def main():
    get_data_file(headers)
    print('I am done')

if __name__ == '__main__':
    main()
