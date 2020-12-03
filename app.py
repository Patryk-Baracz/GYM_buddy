from flask import Flask, request, render_template
from connection import connect


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def game():
    if request.method == 'GET':
        return render_template('index.html')









app.run(debug=True)
