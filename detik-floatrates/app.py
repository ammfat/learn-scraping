from flask import Flask, render_template
from ScrapeDetik import scrape_detik
from ScrapeFloatrates import scrape_floatrates

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/detik-popular')
def home():
    popular_data = get_detik_data()

    return render_template('detik-popular.html', popular_data=popular_data)


@app.route('/idr-rates')
def idr_rates():
    rate_data = get_floatrates_data()

    return render_template('idr-rates.html', rate_data=rate_data)


def get_detik_data():
    url = 'https://www.detik.com/terpopuler'
    params = {'tag_from': 'wp_cb_mostPopular_more'}
    
    sd = scrape_detik.ScrapeDetik(url, params)
    data = { title : (url, image) for title, url, image in zip(sd.titles, sd.urls, sd.images) }

    return data


def get_floatrates_data():
    url = 'http://www.floatrates.com/daily/idr.json'
    sfr = scrape_floatrates.ScrapeFloatrates(url)

    return sfr.get_json_data()


if __name__ == "__main__":
    app.run(debug=False)
