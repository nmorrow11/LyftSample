from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """render text when site is visited"""
    return 'My Lyft Technical Sample'

@app.route('/test', methods = ['POST'])
def sum():
    """return a dictionary of the sum of 2 numbers"""
    content = request.get_json()
    if set(('x', 'y')) <= set(content):
        if isinstance(content['x'], (int, long, float)) and isinstance(content['y'], (int, long, float)):
            answer = {'sum' : content['x'] + content['y']}
            return jsonify(answer)
        else:
            return jsonify('X and/or Y is not a number')
    return jsonify('X and Y are not both keys in the dictionary')

if __name__ == '__main__':
    app.run()