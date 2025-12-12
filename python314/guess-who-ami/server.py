import requests
from flask import Flask, render_template
import datetime

current_year = datetime.datetime.now().year
developer = "Caeser"

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", year=current_year, dev=developer)


@app.route("/guess/<user_name>")
def guess(user_name):
    gender_url = f'https://api.genderize.io?name={user_name}'
    gender_response = requests.get(gender_url, timeout=3)
    gender_data = gender_response.json()
    gender = gender_data['gender']
    age_url = f"https://api.agify.io?name={user_name}"
    age_response = requests.get(age_url, timeout=3)
    age_data = age_response.json()
    age = age_data['age']
    return render_template("guess_user.html", year=current_year, dev=developer, user_name=user_name.title())





if __name__ == "__main__":
    app.run(debug=True, port=8080)
