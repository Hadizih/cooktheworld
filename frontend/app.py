from flask import Flask, render_template, request
from backend.countryhelper import Country

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
            db_path = './backend/data/cdw-database.db'
            name = request.form.get("name")
            if name:
                country = Country.get_country_by_name(name, db_path)
            else:
                country = Country.get_random_country(db_path)
            
            if country:
                return render_template("app.html", random_country=country)
            else:
                return render_template("app.html", error="Country not found")
    
    return render_template("app.html")



if __name__ == "__main__":
    app.run(debug=True)
