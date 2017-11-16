from flask import Flask, render_template,request
from weather_api import main , get_weather
app = Flask(__name__)


@app.route("/" ,methods =['GET' , 'POST'])
def home():
    cities = main()
    if request.method=='POST':
        city = request.form['city_name']
        weather = get_weather(city)
        return render_template('success.html',li=cities, length=range(len(cities))\
                                                                      ,city =weather)
    return render_template("home.html", li=cities, length=range(len(cities)))


if __name__=='__main__':
    app.debug=True
    app.run()
