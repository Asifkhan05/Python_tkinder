import sqlite3

class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()

        qur="""
        create table if not exists emp(
        id Integer primary key,
        name text,
        age text,
        doj text,
        email text,
        gender text,
        contact text,
        address text
        );
        """
        self.cur.execute(qur)
        self.con.commit()
    def insert(self,name,age,doj,email,gender,contact,address):
        qur="insert into emp values(null,?,?,?,?,?,?,?);"
        self.cur.execute(qur,(name,age,doj,email,gender,contact,address))
        self.con.commit()
    def fetch(self):
        qur="select * from emp;"
        self.cur.execute(qur)
        wow= self.cur.fetchall()
        return  wow
    def delete(self,id):
        qur="delete from emp where id=?"
        self.cur.execute(qur,(id,))
        self.con.commit()
    def update(self,id,name,age,doj,email,gender,contact,address):
        qur="update emp set name=?,age=?,doj=?,email=?,gender=?,contact=?,address=? where id=?"
        self.cur.execute(qur,(name,age,doj,email,gender,contact,address,id))
        self.con.commit()

o=Database("emp.db")

