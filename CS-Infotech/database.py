import sqlite3
from datetime import datetime as dt

try:
    with sqlite3.connect(r"C:\Users\Karan\Desktop\ids-python\python-programming\CS-Infotech\mydata.db") as con:
        print("Database connected")

        # To manually add values
        # cmd = "insert into tbemp values(101,'Shalini',120000)"
        # con.execute(cmd)
        # con.commit()
        # print("Data inserted")

        # To insert data with user input
        # cmd1 = "insert into tbemp values(?,?,?)"
        # eno = int(input("Enter employee no.: "))
        # enam = input("Enter employee name: ")
        # esal = int(input("Enter employee salary: "))
        # con.execute(cmd1, (eno,enam,esal))
        # con.commit()
        # print("Data inserted")

        # To bulk insert
        # cmd2 = "insert into tbemp values(?,?,?)"
        # lst = [(104,"Shane",80000),(105,"Parul",30000),(106,"Ranjan",75000)]
        # con.executemany(cmd2, lst)
        # con.commit()
        # print("Data inserted")

        # To retrieve data
        cmd3 = "select * from tbemp order by empnam"
        data1 = con.execute(cmd3) # default is fetchall()
        print(data1.fetchone())
        print(data1.fetchmany(3))
        
        for row in data1:
            print(row[0],row[1],row[2],sep="\t")

except Exception as e:
    print(e)
    with open(r"C:\Users\Karan\Desktop\ids-python\python-programming\CS-Infotech\log.txt",'a') as fp:
        fp.write(str(dt.now())+"    "+str(e)+"\n")
