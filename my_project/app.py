from flask import Flask, render_template
from weather_api import main
app = Flask(__name__)

cities=main()
# print (type(cities))
# print (cities[0]['city'])
# print (cities[0]['temp'])
# print (cities[0]['conditions'])



for i in range (0, len(cities)):
    print (cities[i]['city'])
    print (cities[i]['temp'])
    print (cities[i]['conditions'])


@app.route("/")
def home():
    cities = main()
    return render_template("home.html", li=cities, length=range(len(cities)))


if __name__=='__main__':
    app.debug=True
    app.run()
