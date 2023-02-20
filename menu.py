from collections import defaultdict

MENU_LIST = defaultdict(lambda:MENU_LIST['기본'])

def load_menu(file, key):
    with open(file) as f:
        MENU_LIST[key] = f.read().splitlines()

load_menu('default.txt', '기본')
load_menu('cup-ramen.txt', '컵라면')
load_menu('heaven.txt', '김밥천국')

# unit tests
if __name__ == '__main__':
    print(MENU_LIST['기본'])
    print(MENU_LIST['컵라면'])
    print(MENU_LIST['이상한거'])