from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/products')
def products():
    return "This is the page for the products"


if __name__ == "__main__":
    app.run(debug=True, port=8000)
