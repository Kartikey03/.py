import sqlite3

#connect to database
con=sqlite3.connect("customer.db")

#create a cursor
cur=con.cursor()

#create a table
# cur.execute("""
#             CREATE TABLE customers(
#             first_name text, 
#             last_name text, 
#             email text)""")


#datatypes in sqlite
# 1. null
# 2. integer
# 3. real
# 4. text
# 5. blob

#insert the data
#cur.execute("INSERT INTO customers VALUES('Kartik', 'Sharma', 'kartik@gamail.com')")


#insert many data
# many_customers=[('john', 'wick', 'john@gmail.com'),('haley', 'beiber', 'haley@gmail.com'),('hello', 'yadav', 'hello@gmail.com')]
# cur.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)


#query the database
# cur.execute("SELECT * FROM customers")
# items=cur.fetchall()

# for i in items:
#     print(i[0], i[1], i[2])


cur.execute("")


#commit our command
con.commit()

#close the connection
con.close()