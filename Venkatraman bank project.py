import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="bank",
    auth_plugin='mysql_native_password'
)
n=int(input("1.createaccount 2.balanceenquiry 3.deposit 4.withdrawal"))
if(n==1):
    name=input("enter your name")
    aadhaar=int(input("enter your aadhar details"))
    pan=int(input("enter your pan details"))
    number =("1234567abcdefgh")
    import random
    acclen=7
    accountnumber="".join(random.sample(number,acclen))
    print("your minimum balnace amount is 1000")
    print("please deposit above 1000")
    depositamount=int(input("enter your deposit amount"))
    print("your account created succesfully")
    print("your account number is",accountnumber)
    print("your balance is",depositamount)
    mycursor=mydb.cursor()
    sql="INSERT INTO customerdetails(name,aadhaar,pan,accountnumber,depositamount)VALUES(%s,%s,%s,%s,%s)"
    val=(name,aadhaar,pan,accountnumber,depositamount)
    mycursor.execute(sql,val)
    mydb.commit()
elif(n==2):
    print("you selected balance enquiry")
    n=input("enter your account number")
    mycursor=mydb.cursor()
    sql="SELECT depositamount FROM customerdetails WHERE accountnumber='{}'".format(n)

    mycursor.execute(sql)
    myresult=mycursor.fetchone()
    for x in myresult:
        amount=x
    print("your balance is",amount)
elif(n==3):
    print("you selected deposit option")
    n=input("enter your account number")
    p=int(input("how much money do u need to deposit"))
    mycursor = mydb.cursor()
    sql="SELECT depositamount FROM customerdetails where accountnumber='{}'".format(n)
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    for x in myresult:
        balance = x
    newbalance=p+balance
    mycursor=mydb.cursor()
    sql="UPDATE customerdetails SET depositamount='{}' where accountnumber='{}'".format(newbalance,n)

    mycursor.execute(sql)
    mydb.commit()
elif(n==4):
    print("you selected withdrawl option")
    p=input("enter your account number")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT depositamount FROM customerdetails where accountnumber='{}'".format(p))
    myresult=mycursor.fetchone()
    for x in myresult:
        balance=x
    print("your balance is",balance)
    n=int(input("enter how much money do u need"))
    if(n==balance):
        print("you need sufficent balance")
    elif(n>balance):
        print("insufficient funds")
    else:
        print("your withdrawl ammount is processing")
    newbalance=balance-n
    mycursor=mydb.cursor()
    sql="update customerdetails set depositamount ='{}' where accountnumber='{}'".format(newbalance,p)
    mycursor.execute(sql)
    mydb.commit()
