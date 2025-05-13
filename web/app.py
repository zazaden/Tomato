from flask import Flask, render_template, json, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/Xlebosolniy')
def Xlebosolniy():
    return render_template('Xlebosolniy.html')


@app.route('/Buche')
def Buche():
    return render_template('Bucheserdce.html')


@app.route('/Orlinoe')
def Orlinoe():
    return render_template('Orlinoeserdce.html')


if __name__ == "__main__":
    app.run()
