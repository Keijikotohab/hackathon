import sqlite3

from crud import Sqlite3

dbname = "/app/db/main.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

# sql = 'CREATE TABLE main(id integer primary key,
# img_path string,
# name string,
# weight real default 0,
# has_sent integer check(has_sent=-1 or has_sent=1) default -1,
# step integer default 0);'

sql = 'SELECT * FROM main'
cur.execute(sql)
rows = cur.fetchall()

l = len(rows)+1
# 好きに変えてください

sql = f'UPDATE main SET weight = weight - 1 WHERE has_sent = -1;'
cur.execute(sql)
conn.commit()
print('insert success')


sql = 'SELECT * FROM main'
cur.execute(sql)
rows = cur.fetchall()
print(rows)
cur.close()
conn.close()
