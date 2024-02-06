# GET - Request Data from a specified resoursce 
# POST - create a resource 
# PUT - update a resource
# DELETE - delete a resourse














from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")  #basic
def home():
    return "Hello"


@app.route("/hometwo")
def hometwo():  
    return"home two"


if __name__ == "__main__":
    app.run(debug=True)