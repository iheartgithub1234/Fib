from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
     number = None

     if request.method == "POST":
          number = request.form.get("number")
          number = subprocess.run(["./main", str(number)], capture_output=True, text=True).stdout
          
     return render_template("index.html", number=number)

app.run()