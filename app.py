from flask import Flask,redirect,url_for,render_template,request
from read_horoscope import horoscope

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/",methods=["POST","GET"])
def get_ott():
    if request.method == "POST":
        day = request.form["day"]
        zodiac_sign = request.form["zod"]
        
        return redirect(url_for("display_zodiac_data",day = day,zodiac=zodiac_sign))
    else:
        return render_template("index.html")

@app.route("/<day>/<zodiac>")
def display_zodiac_data(day,zodiac):
    res = horoscope(day,zodiac)
    return render_template("result.html",result = res)

if __name__=="__main__":
    app.run(debug=True)