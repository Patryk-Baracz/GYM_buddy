from flask import Flask, request, render_template
from connection import connect


app = Flask(__name__)

@app.route('/')
def index():
        return render_template('index.html')

@app.route("/pomiar", methods=['GET', 'POST'])
def pomiar():
    if request.method == 'POST':
        pass
    a = render_template('pomiar.html')
    return a









app.run(debug=True)
