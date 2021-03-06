#!/usr/bin/python3
#


from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
@app.route("/test")

#Adding dynamic query

@app.route("/test/<search_query>")

#def search():
#    return "Hello"
def search(search_query):
    return search_query

def hello_world():
    return "Hello,world!"
#####################################
#Appending new dynamic query
#####################################

@app.route("/integer/<int:value>")

def int_type(value):
    print (value + 1)
    return "correct"

@app.route("/float/<float:value>")

def float_type(value):
    print (value + 1)
    return "correct"

#dynamic route that accepts slashes

@app.route("/path/<path:value>")

def path_type(value):
    print (value)
    return "correct"
#Response Object
@app.route("/name/<name>")

def index(name):
    if name.lower() == "michael":
        return "Hello,{}".format(name),200
    else:
        return "Not Found", 404

if __name__ == "__main__":
    app.run()
