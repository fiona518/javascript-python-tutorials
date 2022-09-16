import mysql.connector

myconn = mysql.connector.connect(host = "localhost", user = "root", passwd = "G5g8oqp4!", database="pythonDB2")
  
#creating the cursor object  
cur = myconn.cursor()

try: 
    result = cur.execute("select Employee.id, Employee.name, Employee.salary, Departments.Dept_id, Departments.Dept_Name from Departments left join Employee on Departments.Dept_id = Employee.Dept_id")
    print("ID    Name    Salary    Dept_Id    Dept_Name")  
    for row in cur:  
        print(row[0],"    ", row[1],"    ",row[2],"    ",row[3],"    ",row[4])  
except:
    myconn.rollback()
  
myconn.close()