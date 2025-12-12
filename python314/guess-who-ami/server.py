from flask import Flask, render_template
import datetime
current_year = datetime.datetime.now().year
developer = "Caeser"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html" , year=current_year, dev=developer)


if __name__ == "__main__":
    app.run(debug=True)