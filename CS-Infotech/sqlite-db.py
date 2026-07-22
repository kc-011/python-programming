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
        # cmd3 = "select * from tbemp order by empnam"
        # data1 = con.execute(cmd3) # default is fetchall()
        # print(data1.fetchone())
        # print(data1.fetchmany(3))
        
        # for row in data1:
        #     print(row[0],row[1],row[2],sep="\t")

        # To update data
        # cmd4 = "update tbemp set empsal = ? where empno = ?"
        # con.execute(cmd4,(50000, 103))
        # con.executemany(cmd4,[(30000, 102),(40000,105)])

        # cmd5 = "update tbemp set empsal = 1.10*empsal where empno = ?"
        # con.executemany(cmd5, [(102,),(103,),(105,)])

        # con.commit()

        # To delete data
        # cmd6 = "delete from tbemp where empno = ?"
        # con.execute(cmd6, (101,))
        # con.commit()

except Exception as e:
    print(e)
    with open(r"C:\Users\Karan\Desktop\ids-python\python-programming\CS-Infotech\log.txt",'a') as fp:
        fp.write(str(dt.now())+"    "+str(e)+"\n")
