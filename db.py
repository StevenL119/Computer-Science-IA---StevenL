import sqlite3
con = sqlite3.connect('cycling')
cur = con.cursor()
cur.execute("CREATE TABLE Record1(Time Taken, Start, End)")
cur.execute("CREATE TABLE Record2(Distance Travelled, Average Speed, Highest Speed)")
