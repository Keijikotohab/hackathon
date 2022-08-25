import sqlite3

from main.crud import Sqlite3

dbname = "/app/db/main.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

sql = 'drop table if exists main'

cur.execute(sql)

sql = 'CREATE TABLE main(id integer primary key, img_path string, name string, weight real default 0, has_sent integer check(has_sent=-1 or has_sent=1) default -1, step integer default 0);'

cur.execute(sql)

conn.commit()
print('init success')
cur.close()
conn.close()

sq = Sqlite3()
sq.connect()
sq.create()

