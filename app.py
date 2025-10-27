from flask import Flask, render_template

app = Flask(__name__)

# მთავარი გვერდი
@app.route("/")
def home():
    cars = [
        {"brand": "BMW", "model": "M3", "price": 22000},
        {"brand": "Mercedes", "model": "C300", "price": 18000},
        {"brand": "Audi", "model": "A6", "price": 15000},
    ]
    return render_template("home.html", cars=cars)

# ჩვენს შესახებ
@app.route("/about")
def about():
    company_info = {
        "name": "Auto_World_Georgia",
        "founded": 2015,
        "mission": "მაღალი ხარის მომსახურება ლოიალურ ფასებში."
    }
    return render_template("about.html", info=company_info)

# კონტაქტი
@app.route("/contact")
def contact():
    contact_methods = ["Email: info@Auto_World_Georgia.ge", "Tel: +995 555 123 456", "Address: თბილისი, საბურთალო"]
    return render_template("contact.html", contacts=contact_methods)

if __name__ == "__main__":
    app.run(debug=True)
