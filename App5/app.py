from flask import Flask, render_template, request, json, jsonify


app = Flask(__name__)
data = []

file = open("data.json", "r")
# data = file.read()

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        return f"<h1>Name: {name}</h1>"
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)