from flask import Flask, render_template            # from the flask "module import the Flask class"

app = Flask(__name__)                               #Instantiate the Flask class into the app variable (object)



@app.get("/")                                       #decorator that allows us to map routes to "view functions"
def index():                                        #Flask calls these "view functions"
    return render_template ("/index.html")           #return statement

@app.get("/objects")
def objects():
    return render_template ("/objects.html")

@app.get("/classes")
def classes():
    return "<h1>Classes Page</h1>"

@app.get("/about")
def about():
    me = {
        "first_name": "Mark",
        "last_name": "Ortiz",
        "hobbies": "video games",
        "bio": "I'm a student of tech who's trying to learn coding but is lost most of the time."
    }
    return render_template ("/about.html", about_dict=me)