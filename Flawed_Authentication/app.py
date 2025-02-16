from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if "admin" in username and password == "secret":
        return render_template("success.html", flag="asthra{Weak_Login_Bug}")
    else:
        return render_template("index.html", error="Invalid credentials! Try again.")

if __name__ == "__main__":
    app.run(debug=True)
