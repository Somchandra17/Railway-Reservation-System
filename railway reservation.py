

def menu():
    print('1.YES')
    print('2.NO')
    ch=int(input('DO YOU WANT TO CONTINUE OR NOT:'))
    while ch==1:
        print('WELECOME TO ONLINE RAILWAY RESERVATION SYSTEM') 
        print('1.SIGN IN')
        print('2.SIGN UP')
        print('3.DELETE ACCOUNT')
        print('4.EXIT')
        ch1=int(input('ENTER YOUR CHOICE:'))
        if ch1==1:
            a=checking()
            if a==True:
                print('WELCOME')
                main()
            else:
                
                continue
        elif ch1==2:
            a=checking_1()
            if a==True:
                main()
            else:
                print('PASSWORD ALREADY EXISTS')
                continue
            
            
        elif ch1==3:
            c=checking_2()
            if c==True:
               
                print('ACCOUNT DELETED')
                continue
            else:
                print('YOUR PASSWAORD OR USER_NAME IS INCORRECT')
                continue
        elif ch1==4:
            print('THANK YOU')
            break
        else:
            print('ERROR 404:PAGE NOT FOUND')
            break
def main():        
    print('1.yes')
    print('2.no')
    c=int(input("do you want to continue or not:"))
    while (c==1):
        print(' 1.TICKET BOOKING',"\n", '2.TICKET CHECKING',"\n",'3.TICKET CANCELLING',"\n",'4.ACCOUNT DETAILS',"\n",'5.LOG OUT')
        ch=int(input('enter ur choice:'))
        if ch==1:
            ticket_booking()
        elif ch==2:
            ticket_checking()
        elif ch==3:
            ticket_cancelling()
        elif ch==4:
            checking_3()
            
                
        elif ch==5:
            print('THANK YOU')
            break
        else:
            print('WRONG INPUT')
    else:
        print('ERROR 404: ERROR PAGE NOT FOUND')
def ticket_booking():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='root',database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    nm=input('enter your name:')
    phno=input('enter your phone number:')
    age=int(input('enter your age:'))
    print(' M=MALE','\n','F=FEMALE','\n','N=NOT TO MENTION')
    gender=input('enter your gender:')
    Gender=gender.upper()
    fr=input('enter ur starting point:')
    to=input('enter your destination:')
    date1=input('enter date(dd):')
    date2=input('enter month(mm):')
    date3=input('enter year(yyyy):')
    date=date1+"/"+date2+"/"+date3
    a={'M':'MALE','F':'FEMALE','N':'NOT TO MENTION'}
    v=a[Gender]
    s1="insert into railway values('{}',{},{},'{}','{}','{}','{}')".format(nm,phno,age,v,fr,to,date)
    cursor.execute(s1)
    print('BOOKED SUCCESSFULLY')
def ticket_checking():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='root',database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    print('1.yes')
    print('2.no')
    ch=int(input("do you want to continue or not:"))

    if ch==1:
        phno=int(input('enter your phnone number:'))
        try:
            s1="select * from railway where phno=phno"
            cursor.execute(s1)
            data=cursor.fetchall()[0]
            Data=list(data)
            a=['NAME','PHONE NUMBER','AGE','GENDER','STARTING POINT','DESTINATION','DATE',]
            print(a[0],'::::',Data[0].upper())
            print(a[1],'::::',Data[1])
            print(a[2],'::::',Data[2])
            print(a[3],'::::',Data[3].upper())
            print(a[4],'::::',Data[4].upper())
            print(a[5],'::::',Data[5].upper())
            print(a[6],'::::',Data[6])
        except:
            print('TICKET DOES NOT EXISTS')
    elif ch==2:
        print('THANK YOU')
    else:
        print('ERROR 404:PAGE NOT FOUND')
    
       

def ticket_cancelling():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='root',database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    print('1.yes')
    print('2.no')
    ch=int(input("do you want to continue or not:"))
    if ch==1:
        phno=input('enter your phone number:')
        s1="delete from railway where phno=phno"
        cursor.execute(s1)
        print('TICKET CANCELLED')
    elif ch==2:
        print('THANK YOU')
    else:
        print('ERROR 404:PAGE NOT FOUND')
        
def checking_2():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='root',database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    a=input('USER NAME:')
    b=input('PASS WORD:')
    try:
        s1="select user_name from user_accounts where password='{}'".format(b)
        cursor.execute(s1)
        data=cursor.fetchall()[0]
        data=list(data)
        if data[0]==a:
             print('IS THIS YOUR ACCOUNT')
             s1="select user_name from user_accounts where password='{}'".format(b)
             c1="select fname,lname from user_accounts where password='{}'".format(b)
             cursor.execute(c1)
             data1=cursor.fetchall()[0]
             data1=list(data1)
             data1=data1[0]+' '+data1[1]
             cursor.execute(s1)
             data=cursor.fetchall()[0]
             data=list(data)
             if data[0]==a:
                 x=['FIRST NAME','LAST NAME','PHONE NUMBER','GENDER','DATE OF BIRTH','AGE']
                 s1="select fname,lname,phno,gender,dob,age from user_accounts where password='{}'".format(b)
                 cursor.execute(s1)
                 data=cursor.fetchall()[0]
                 data=list(data)
                 print(x[0],':::',data[0])
                 print(x[1],':::',data[1])
                 print(x[2],':::',data[2])
                 print(x[3],':::',data[3])
                 print(x[4],':::',data[4])
                 print(x[5],':::',data[5])
                 print('1.yes')
                 print('2.no')
                 vi=int(input('enter your choice:'))
                 if vi==1:
                     b1="delete from user_accounts where password = '{}'".format(b)
                     cursor.execute(b1)
                     return True
                 elif vi==2:
                     print('SORRY,RETRY')
                 else:
                     print('ERROR 404:PAGE NOT FOUND')
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')
        

def checking_1():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='root',database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    f=input("FIRST NAME:")
    l=input("LAST NAME:")
    n=f+" "+l
    a=input('USER NAME:')
    b=input('PASS WORD:')
    c=input('RE-ENTER YOUR PASS WORD:')
    ph=input("PHONE NUMBER:")
    print(' M=MALE','\n','F=FEMALE','\n','N=NOT TO MENTION')
    gen=input('ENTER YOUR GENDER:')
    print("ENTER YOR DATE OF BIRTH")
    d=input("DD:")
    o=input("MM:")
    p=input("YYYY:")
    dob=d+'/'+o+'/'+p
    age=input('YOUR AGE:')
    v={'m':'MALE','f':'FEMALE','n':'NOT TO MENTION'}
    if b==c:
        try:
            c1="insert into user_accounts values('{}','{}','{}','{}','{}','{}','{}','{}')".format(f,l,a,b,ph,v[gen],dob,age)
            cursor.execute(c1)
            print('WELCOME',f,' ',l)
            return True
        except:
            print('PASSWORD ALREADY EXISTS')
            return False
    else:
        print('BOTH PASSWORDS ARE NOT MATCHING')
        


def checking():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='root',database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    a=input('USER NAME:')
    b=input('PASS WORD:')
    try:
        s1="select user_name from user_accounts where password='{}'".format(b)
        c1="select fname,lname from user_accounts where password='{}'".format(b)
        cursor.execute(c1)
        data1=cursor.fetchall()[0]
        
        data1=list(data1)
        data1=data1[0]+' '+data1[1]
        cursor.execute(s1)
        data=cursor.fetchall()[0]
        data=list(data)[0]
        if data==a:
            print(' HII ',data1)
            return True
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')

def checking_3():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='root',database='railway')
    cursor=mycon.cursor()
    mycon.autocommit=True
    a=input('USER NAME:')
    b=input('PASS WORD:')
    try:
        s1="select user_name from user_accounts where password='{}'".format(b)
        c1="select fname,lname from user_accounts where password='{}'".format(b)
        cursor.execute(c1)
        data1=cursor.fetchall()[0]
        data1=list(data1)
        data1=data1[0]+' '+data1[1]
        cursor.execute(s1)
        data=cursor.fetchall()[0]
        data=list(data)
        if data[0]==a:
            
            x=['FIRST NAME','LAST NAME','PHONE NUMBER','GENDER','DATE OF BIRTH','AGE']
            s1="select fname,lname,phno,gender,dob,age from user_accounts where password='{}'".format(b)
            cursor.execute(s1)
            data=cursor.fetchall()[0]
            data=list(data)
            print(x[0],':::',data[0])
            print(x[1],':::',data[1])
            print(x[2],':::',data[2])
            print(x[3],':::',data[3])
            print(x[4],':::',data[4])
            print(x[5],':::',data[5])
            
            
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')

menu()
    
    
    

            
        
        
    
    
    
    
    
