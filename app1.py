#!/usr/bin/python3


from flask import Flask

app = Flask(__name__)
#error handling
app.config["DEBUG"] = True


@app.route("/")
@app.route("/hello")

#define the view using a function,which return a string

def hello_world():
    return "Hello,world!"

#dynamic route

@app.route("/test/<search_query>")
def search(search_query):
    return search_query

#dynamic route with explicit status code
@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael":  # notice that the usage of lower and "=="
        return "Hello.{}".formate(name)
    else:
        return "Not Found",404


if __name__ == "__main__":
    app.run()
