# sqlite
# lib for work with sqlite

import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

# create table
cursor.execute('''CREATE TABLE IF NOT EXISTS stocks 
(date text, trans text, symbol text, qty real, price real)''')

# insert data
cursor.execute("INSERT INTO stocks VALUES ('2021-01-01', 'BUY', 'RHAT', 100, 35.14)")

# commit changes
conn.commit()

# close connection (if not commit before it all new data will be lost)
# conn.close()

# sent data to query
t = ('RHAT',)
cursor.execute('SELECT * FROM stocks WHERE symbol=?', t)
# print(cursor.fetchone())

purshases = [('2021-01-01', 'BUY', 'IBM', 1000, 45.00),
             ('2021-02-02', 'BUY', 'MSFT', 2000, 72.01),
             ('2021-03-03', 'SELL', 'IBM', 500, 53.43),
             ]

cursor.executemany('INSERT INTO stocks VALUES (?, ?, ?, ?, ?)', purshases)

for row in cursor.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)
