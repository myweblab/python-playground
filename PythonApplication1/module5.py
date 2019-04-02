import sqlite3
try:
    con = sqlite3.connect('test.db')
    help(con)
    cursor = con.cursor()
    cursor.execute("SELECT SQLITE_VERSION()")
    data = cursor.fetchone()
    print(str(data))
    cursor.execute('CREATE TABLE EMPLOYEE(NAME TEXT, SALARY INT)')
    cursor.execute("INSERT INTO EMPLOYEE('SAMMY', '2000')")
    cursor.execute("INSERT INTO EMPLOYEE('DAMMY', '3000')")
    cursor.execute("INSERT INTO EMPLOYEE('MAMMY', '5000')")
    con.commit()
    cursor.execute('SELECT * FROM EPMLOYEE')
    data = cursor.fetchall()
    print(str(data))
except:
    pass
finally:
    con.close()