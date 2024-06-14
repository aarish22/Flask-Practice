from flask import Flask, redirect, url_for
import time

app = Flask(__name__)

@app.route('/')
def homepage():
    return "<h1>Welcome</h1>"

@app.route('/score/<name>/<int:num>')
def score(name, num):
    time.sleep(2)
    if num > 30:
        return redirect(url_for("passed", s_name=name , marks=num))
    else:
        return redirect(url_for("failed", s_name=name , marks=num))

@app.route('/pass/<s_name>/<int:marks>')
def passed(s_name,marks):
    return f"<h1>{s_name.title()} has passed, scoring {marks} marks</h1>"

@app.route('/fail/<s_name>/<int:marks>')
def failed(s_name,marks):
    return f"<h1>{s_name.title()} has failed, scoring {marks} marks</h1>"

if __name__ == "__main__":
    app.run(debug=True)
