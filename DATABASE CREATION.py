def Create_Database_Railway():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='root')    
    cursor=mycon.cursor()
    mycon.autocommit=True
    s1="create database railway"
    cursor.execute(s1)
Create_Database_Railway()
