from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)
#this route prints text when you go to the page
@app.route('/')
def index():
    return 'My first flask app'

#this is the test route that takes 2 numbers and returns a dictionary of their sum
@app.route('/test', methods = ['POST'])
def sum():
    content = request.get_json()
    if set(('x', 'y')) <= set(content):
        if isinstance(content['x'], (int, long, float)) and isinstance(content['y'], (int, long, float)):
            answer = {'sum' : content['x'] + content['y']}
            return jsonify(answer)
        else:
            return jsonify('X and/or Y is not a number')
    return jsonify('X and Y are not both keys in the dictionary')

if __name__ == '__main__':
    app.run(debug=True)