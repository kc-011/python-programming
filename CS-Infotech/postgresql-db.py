import psycopg2
from configparser import ConfigParser

def config_info(filename, section):
    parser = ConfigParser()
    parser.read(filename)
    db={}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]]=item[1]
    return db
    
db = config_info(r"C:\Users\Karan\Desktop\ids-python\python-programming\CS-Infotech\settings.ini",'postgresql')
def connect():
    con = psycopg2.connect(**db)
    return con

try:
    con=connect()
    print("Connected")
except Exception as e:
    print(e)

try:
    # To insert data
    # cmd = "insert into tbstu values(%s,%s,%s)"
    # cur=con.cursor()
    # cur.execute(cmd, (101,"Shalini",47))
    # con.commit()
    # print('Data stored')

    # To select data
    cmd1 = "select * from tbstu order by stu_name"
    cur=con.cursor()
    cur.execute(cmd1)
    rows=cur.fetchall()
    for row in rows:
        print(row[0],row[1],row[2],sep="\t")

except Exception as e:
    print(e)