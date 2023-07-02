

# connect to database


import sqlite3

con = sqlite3.connect('../databases/orders.db')

cur = con.cursor()

# res = cur.execute("SELECT * FROM status_enum2;")
# print(res.fetchall())




