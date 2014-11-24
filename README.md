FlaskFunStuff
=============

Flasky stuff

///data base test stuff
import sqlite3
#conn = sqlite3.connect('test.db')
#c = conn.cursor()

# Create table
#c.execute('''CREATE TABLE stocks
#             (Id INTEGER PRIMARY KEY AUTOINCREMENT,Parent int,Rating int,Body text)''')

# Insert a row of data
#c.execute("INSERT INTO stocks(Parent,Rating,Body) VALUES ('1','5','it fell off its hinges')")

# Save (commit) the changes
#conn.commit()
#conn.close()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn = sqlite3.connect('test.db')
c = conn.cursor()
t = ('1',)
c.execute('SELECT * FROM stocks WHERE Parent=?', t)
rows = c.fetchall()
for row in rows:
	print (row)



