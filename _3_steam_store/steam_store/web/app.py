from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def index():
    resp = requests.get(
        url = 'http://localhost:9080/crawl.json?start_requests=true&spider_name=index'
    ).json()
    items = resp.get('items')
    return render_template('index.html', games=items) 


    

if __name__ == '__main__':
    app.run(debug=True)