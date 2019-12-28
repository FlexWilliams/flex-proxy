import logging
import requests
from flask import Flask, abort, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/food-search', methods = [ 'GET' ])
def get():
    food = request.args.get('food')
    if food is None or food == "":
        return abort(400)
    else:        
        url = 'https://api.nal.usda.gov/fdc/v1/search?api_key=L196LsvJyUTSZmzkW8N78dNgcEcR0Dx1wL8cRzF8'
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json = { 'generalSearchInput': food })
                
        return response.json()

if __name__ == '__main__':
   app.run()