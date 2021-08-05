from flask import Flask, render_template
from ScrapDetik import scrap_detik

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detik-popular')
def home():
    popular_data = get_data()

    return render_template('detik-popular.html', popular_data=popular_data)


def get_data():
    url = 'https://www.detik.com/terpopuler'
    params = {'tag_from': 'wp_cb_mostPopular_more'}
    
    sd = scrap_detik.ScrapDetik(url, params)
    data = { title : (url, image) for title, url, image in zip(sd.titles, sd.urls, sd.images) }

    return data

if __name__ == "__main__":
    app.run(debug=True)
