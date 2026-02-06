from flask import Flask, render_template, url_for

app = Flask(__name__)


products = {
    "black-shirt": {
        "name": "Black T-Shirt",
        "price": 253000,
        "image": "Assets/Auro_Shirt_Black.png",
        "description": "Premium black cotton t-shirt"
    },
    "white-shirt": {
        "name": "White T-Shirt",
        "price": 253000,
        "image": "Assets/Auro_Shirt_White.png",
        "description": "Clean white cotton t-shirt"
    },
    "orange-shirt":{
        "name": "Orange T-Shirt",
        "price": 253000,
        "image": "Assets/Auro_Shirt_Orange.png",
        "description": "Bright orange cotton t-shirt"
    },
    "orange-shirt1":{
        "name": "Orange T-Shirt",
        "price": 253000,
        "image": "Assets/Auro_Shirt_Orange.png",
        "description": "Bright orange cotton t-shirt"
    },
    "orange-shirt2":{
        "name": "Orange T-Shirt",
        "price": 253000,
        "image": "Assets/Auro_Shirt_Orange.png",
        "description": "Bright orange cotton t-shirt"
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/catalog')
def catalog():
    return render_template('Catalog.html', products=products)

@app.route('/about_us')
def about_us():
    return render_template('About_Us.html')

@app.route('/product_page/<product_id>')
def product_page(product_id):
    product = products.get(product_id)

    if not product_page:
        return "Not Found", 404
    
    return render_template("product.html", 
                           product=product,
                           product_id = product_id)

@app.route('/buy_page/<product_id>')
def buy_page(product_id):    
    product = products.get(product_id)

    if not product:
        return "Not Found", 404
    
    return render_template('Buy_Page.html', product=product)

if __name__ == "__main__":
    app.run(debug=True)