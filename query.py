import sqlite3
import pandas as pd
conn=sqlite3.connect("factbook.db")
data=conn.execute("select name from facts order by population asc limit 10;").fetchall()
print (data)


