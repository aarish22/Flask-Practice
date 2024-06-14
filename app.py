from flask import Flask,render_template
from employees import employees_data

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html',title="HomePage")


@app.route("/about")
def about():
    return render_template('about.html',title="About")

@app.route("/welcome")
def welcome():
    return f"<h1>Hi, welcome to our page!</h1>"

@app.route("/evaluate/<int:num>")
def evaluate(num):
    return render_template('evaluate.html',title="Evaluation",number=num)

@app.route("/employees")
def employees():
    return render_template('employees.html',title="Employee_Data",employees=employees_data)

@app.route("/employees/managers")
def managers():
    return render_template('manager.html',title="Manager",employees=employees_data)

    
if __name__ == "__main__":
    app.run(debug=True)