from flask import Flask,redirect,url_for,render_template
import json

app = Flask(__name__)




@app.route("/")
def home():
    return render_template("parallax.html", context=len(data_dict))



data_JSON =  """
[
	{
    "name": "Bonda",
    "post":"secure",
    "link":"www.google.com"
    },
    {
    "name": "Bunda",
    "post":"secure",
    "link":"www.google.com"
    },
    {
    "name": "ponda",
    "post":"secure",
    "link":"www.google.com"
    },
    {
    "name": "konda",
    "post":"secure",
    "link":"www.google.com"
    },
    {
    "name": "Banda",
    "post":"secure",
    "link":"www.google.com"
    },
    {
    "name": "londa",
    "post":"secure",
    "link":"www.google.com"
    }
]
"""



# Convert JSON string to dictionary
data_dict = json.loads(data_JSON)
print(data_dict[1]['name'])

if __name__ == "__main__":
    app.run()