from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

@app.route("/")
def input():
    '''
    if name in request.args:
        name = request.args["name"]
    else:
        name = "world"
    '''
    name = request.args.get("name","world")
    return render_template("index.html", name = name)

@app.route("/registrants", methods=["POST"])
def registrants():
    if request.method =="POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("layout.html", name = name)


