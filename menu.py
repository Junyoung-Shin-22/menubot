import requests

url = "http://dogumaster.com/select/menu/api"
headers = {
        'Host': 'dogumaster.com',
        'Origin': 'http://dogumaster.com',
        'Referer': 'http://dogumaster.com/select/menu',

        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Whale/3.22.205.18 Safari/537.36',
        'Content-type': 'application/x-www-form-urlencoded',
    }
data = {
        'type_01': 'all',
        'country': 'all',
        'type_03': 'all',
    }

def get_menu():
    response = requests.post(url=url, headers=headers, data=data)
    if response.status_code == 200:
        try:
            return response.json()['name']
        except:
            return None

if __name__ == '__main__':
    for _ in range(10):
        print(get_menu())