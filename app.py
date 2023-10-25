from flask import Flask, render_template, request, flash
from weather import get_current_weather_data as wetter

app = Flask(__name__)
app.config['SECRET_KEY'] = 'WERAGAERGQERG'

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        country_code = request.form['country_code']
        city_name = request.form['city_name']
        if country_code and city_name:
            if wetter(country_code, city_name) == 0:
                flash(message='Es gab ein Problem, versuchen Sie noch mal bitte !')
            else:
                wd = wetter(country_code, city_name)
                return render_template('index.html', weather_data=wd, city_name=city_name)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=1000)
