from flask import *
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form["name"])
        print(request.form["email"])  

    return render_template("home.html")


@app.route("/get_status", methods=["GET"])
def get_order_status():
    args = request.args
    print(args.get('id')) 

    # TODO: Write DB query here
    return 'Sucesss'


if __name__ == "__main__":
    app.run()
