from crud import Sqlite3

imgs = Sqlite3().read()

for img in imgs:
    print('img')
    print(img)
