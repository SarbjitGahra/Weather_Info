from flask import Flask, render_template
from weather_api import main
app = Flask(__name__)


@app.route("/")
def home():
    cities = main()
    return render_template("home.html", li=cities, length=range(len(cities)))


if __name__=='__main__':
    app.debug=True
    app.run()
