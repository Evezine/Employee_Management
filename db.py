import sqlite3

class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur = self.con.cursor()# we can execute all query from cursor() object
        sql="""
        CREATE TABLE IF NOT EXISTS employees ( 
               id Integer Primary Key,
               name text ,
               age text,
               doj text,
               email text,
               gender text,
               contact text,
               address text
               )
               """
        self.cur.execute(sql)
        self.con.commit()
    #insert function
    def insert(self,name,age,doj,email,gender,contact,address):
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?)",
                         (name,age,doj,email,gender,contact,address))
        self.con.commit()


     #Fetch All Data   from db
    def fetch(self):
        self.cur.execute("select * from  employees")
        rows=self.cur.fetchall()
        #print(rows)
        return rows
    
     #Delete a record in db
    def remove(self,id):
         self.cur.execute("delete from employees where id=?",(id,))
         self.con.commit()


     #Update a record in db
    def update(self,id,name,age,doj,email,gender,contact,address):
        self.cur.execute("update employees set name=?,age=?,doj=?,email=?,gender=?,contact=?,address=? where id=?",
                         (name,age,doj,email,gender,contact,address,id))
        self.con.commit()
o=Database("Employee.db")        
#o.insert("Raghu",22,"22-12-2001","raghu@gmail.com","male","6374353482","ashok street,chennai")
#o.fetchall()
#o.remove("5")
#o.update("3","sam kumar",20,"02-06-2023","sam@gmail.com","male","7904263599","ravathur street,salem")
