from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
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

if __name__ == "__main__":
    app.run(debug=True)