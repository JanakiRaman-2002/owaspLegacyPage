from flask import Flask,redirect,url_for,render_template
import json

app = Flask(__name__)
# JSON
jsonfile = open("hoomans.json",'r')
jsondata = jsonfile.read()

# Parse JSON
obj = json.loads(jsondata)
members = obj["members"]

@app.route("/")
def home():
    return render_template("parallax.html", context=members)

if __name__== "__main__":
    app.run()