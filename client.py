from flask import Flask
from flask import render_template
import requests
import upstream

app = Flask(__name__)

def get_products():
    products = requests.get(upstream.get_product_addr())
    print(products.status_code)
    print(products.text)
    return products.json()

def get_listings():
    listings = requests.get(upstream.get_product_addr())
    print(listings.status_code)
    print(listings.text)
    return listings.json()

@app.route('/healthz')
def healthz():
    return 'OK'

@app.route('/')
def index():
    products = get_products()
    listings = get_listings()
    return render_template('index.html', prod_list=products, listings_list=listings)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)
