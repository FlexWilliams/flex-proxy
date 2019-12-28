from flask import Flask, abort, request
app = Flask(__name__)

@app.route('/', methods = [ 'GET' ])
def get():
    url = request.args.get('url')
    if url is None or url == "":
        return abort(400)
    else:
        return url
    
    # r = requests.get(url)
    # return r.text

if __name__ == '__main__':
   app.run()