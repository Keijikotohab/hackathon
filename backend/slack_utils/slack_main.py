import sqlite3

dbname = "main.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()


sql = 'select * from main; '

cur.execute(sql)

all_data = cur.fetchall()
print(all_data)

cur.close()
conn.close()
