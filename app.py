#import flask and its component 
from flask import *

#import the pymysql module- it help us create  connection between pyton flask and mysql database
import pymysql

#create a flask application and give it a name
app =Flask (__name__)


#below is the sign up route
@app.route("/api/signup", methods = ["POST"])
def signup():
    if request.method == "POST":
        #extract the different details entered on the form
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        phone = request.form["phone"]

        #by use of the print function lets print all those details sent with the upcoming request
        #print( username , email , password , phone)

        #establish a connection between flask/python and mysql
        connection = pymysql.connect(host="localhost", user="root", password="", database="sokogardenonline")

        #create a cursor to execute the sql queries
        cursor = connection.cursor()

        #structure an sql to insert the details received from the form
        #the %s is a placeholder -> a placeholder it stands in places of actual values
        sql = "INSERT INTO users(username,email,phone,password) VALUES(%s,%s,%s,%s)"

        #create a tuple that will hold all the data gotten from the form
        data =(username , email ,phone,password)

        #by use of the cursor , execute the sql as you replace the placeholder with the actual values
        cursor.execute(sql,data)

        #commit the changes to the database
        connection.commit()


        return jsonify({"message" : "User registered successfully"})










#run application
app.run(debug = True)