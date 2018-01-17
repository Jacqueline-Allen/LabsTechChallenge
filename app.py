from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route("/ja3143")
def uni():
    return render_template('uni.html')

if __name__ == '__main__':
    app.run()
