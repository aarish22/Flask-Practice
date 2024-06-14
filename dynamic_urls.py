from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return "<h1>Welcome<h1/>"

@app.route('/welcome/<name>')
def welcomeSuperhero(name):
    return f"<h1>Hey {name.title()}, welcome to our page</h1>"

if __name__ == "__main__":
    app.run(debug=True)