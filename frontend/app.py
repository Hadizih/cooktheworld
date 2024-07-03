from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about", methods=['GET', 'POST'])    
def about():
    return render_template("about.html")

@app.route("/app", methods=['GET', 'POST'])
def ctw_app():
    if request.method == 'POST':
        pass
    return render_template("app.html")


if __name__ == "__main__":
    app.run(debug=True)
