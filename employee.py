import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='sample2'
)



def list():
    mycr = mydb.cursor()
    mycr.execute("select * from employee")
    for i in mycr:
        print(i)

def add():
    mycr = mydb.cursor()
    s1 = 'insert into employee values(%s,%s,%s,%s)'
    Eid = int(input('Id :'))
    Ename = input('Name :')
    Eage = int(input("Age :"))
    Esal = int(input("Salary :"))
    v1=(Eid,Ename,Eage,Esal)
    mycr.execute(s1,v1)
    mydb.commit()
    print("Added Successfully...")
def edit():
    mycr = mydb.cursor()
    ed = int(input("Enter the id to edit :"))
    Ename = input('Name :')
    Eage = int(input("Age :"))
    Esal = int(input("Salary"))
    mycr.execute("update employee set  NAME = %s,Age = %s,Salary = %s where id = %s ",(Ename,Eage,Esal,ed))
    mydb.commit()
    print("Updated Successfully...")
def delete():
    mycr = mydb.cursor()
    eid =int(input("Enter the id to delete :"))
    mycr.execute("delete from employee where id =%s",(eid,))
    mydb.commit()
    print("Deleted Successfully...")

c = 6
while c != 5 :
    print("MENU")
    print("Please select your input ")
    print("\n1.List \n2.Add \n3.Edit \n4.Delete \n5.Exit")
    c = int(input("Enter the Choice :"))
    if c == 1:
        list()
    elif c == 2:
        add()
    elif c == 3:
        edit()
    elif c == 4:
        delete()
    else:
        print("Invalid option ...")