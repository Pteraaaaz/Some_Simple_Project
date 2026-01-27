from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/catalog')
def catalog():
    return render_template('Catalog.html')

@app.route('/about_us')
def about_us():
    return render_template('About_Us.html')
if __name__ == "__main__":
    app.run(debug=True)