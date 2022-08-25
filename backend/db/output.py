import sqlite3

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

for row in rows:
    print(row)
cur.close()
conn.close()

