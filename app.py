#import flask and its component 
from flask import *         #(Hey Flask, I want to use your tools to build my website!)



#import the pymysql module- it help us create  connection between python flask and mysql database
import pymysql       #(helps python to talk to my database-mysql)

#create a flask application and give it a name
app =Flask (__name__)    #(this creates your website)


#below is the sign up route
@app.route("/api/signup", methods = ["POST"])   #(when sb goes to /api/signup and sends info using post , we will run the signup function)
def signup():    #(helps one register)
    if request.method == "POST":
        #extract the different details entered on the form
        #(details)
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        phone = request.form["phone"]

        #by use of the print function lets print all those details sent with the upcoming request
        #print( username , email , password , phone)

        #establish a connection between flask/python and mysql
        connection = pymysql.connect(host="localhost", user="root", password="", database="sokogardenonline")   #(we can write inside)

        #create a cursor to execute the sql queries
        cursor = connection.cursor()    #(pen for writing)

        #structure an sql to insert the details received from the form
        #the %s is a placeholder -> a placeholder it stands in places of actual values
        sql = "INSERT INTO users(username,email,phone,password) VALUES(%s,%s,%s,%s)"    # (insert->add a new row in the users table) (%s->empty boxes waiting for real values)

        #create a tuple that will hold all the data gotten from the form
        data =(username , email ,phone,password)    #(we put real info into the empty boxes)

        #by use of the cursor , execute the sql as you replace the placeholder with the actual values
        cursor.execute(sql,data)

        #commit the changes to the database
        connection.commit() #(saving permanently)


        return jsonify({"message" : "User registered successfully"})   #(Yaaay! The new friend has joined successfully!)










#run application
app.run(debug = True)