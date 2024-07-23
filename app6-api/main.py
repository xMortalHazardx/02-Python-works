import pandas
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<word>/<definition>")
def about(word, definition):
    palavra = word.upper()
    definicao = definition.upper()
    return {"word": palavra,
            "definition": definicao,
            }

if __name__ =="__main__":
    app.run(debug=True, port=5001)