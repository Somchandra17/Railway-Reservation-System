def connection():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='root',database='railway')
    if mycon.is_connected():
        print("successfully connected")
connection()
