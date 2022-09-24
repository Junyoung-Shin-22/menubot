from collections import defaultdict

MENU_LIST = defaultdict(lambda:MENU_LIST['기본'])

with open('default.txt') as f:
    MENU_LIST['기본'] = f.read().splitlines()

with open('cup-ramen.txt') as f:
    MENU_LIST['컵라면'] = f.read().splitlines()

if __name__ == '__main__':
    print(MENU_LIST['기본'])
    print(MENU_LIST['컵라면'])
    print(MENU_LIST['이상한거'])