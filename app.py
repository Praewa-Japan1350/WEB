from flask import Flask, render_template, request, redirect, url_for, session
from flask import flash

app = Flask(__name__)
app.secret_key = "secret123"

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # ตัวอย่างตรวจสอบแบบง่าย
        if username == "admin" and password == "1234":
            session["user"] = username
            return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    error = None

    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        student_id = request.form["student_id"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if len(password) < 6:
            error = "Password must be at least 6 characters."

        elif password != confirm_password:
            error = "Passwords do not match."

        else:
            return redirect(url_for("login"))

    return render_template("register.html", error=error)

@app.route("/reset-password", methods=["GET", "POST"])
def reset_password():
    if request.method == "POST":
        new_password = request.form["new_password"]
        confirm_password = request.form["confirm_password"]

        if new_password != confirm_password:
            return render_template("reset_password.html")

        return redirect("/login")

    return render_template("reset_password.html")

@app.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form["email"]
        return redirect(url_for("reset_password"))

    return render_template("forgot_password.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)