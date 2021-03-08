#   importing necessary module
from flask import Flask
from flask import render_template

#   passing the flaskapp through 'app' variable
app = Flask(__name__)


#   default route
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)