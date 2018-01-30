from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """ Render text when site is visited. """
    return 'My Lyft Technical Sample.'

@app.route('/test', methods = ['POST'])
def sum():
    """ Return a dictionary of the sum of 2 numbers. """
    content = request.get_json()
    x = content['x']
    y = content['y']
    """ Check if x and y are keys and data types that can be added. """
    if set(('x', 'y')) <= set(content):
        if isinstance(x, (int, long, float)) and isinstance(y, (int, long, float)):
            answer = {'sum' : x + y}
            return jsonify(answer)
        else:
            return jsonify('x and/or y is not an int, long, or float.')
    return jsonify('x and y are not both keys in the dictionary.')

if __name__ == '__main__':
    app.run()
