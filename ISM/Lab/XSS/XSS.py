from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test', methods=['POST'])
def test():
    input_string = request.form['input_string']
    return render_template('test.html', input_string=input_string)

if __name__ == '__main__':
    app.run(debug=True)
