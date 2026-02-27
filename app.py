from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# ข้อมูลตัวอย่างสำหรับแสดงในหน้า Dashboard และ Assignment
tasks = [
    {
        "id": 1,
        "title": "Math Homework 4",
        "subject": "Calculus",
        "due": "28 Feb, 2026",
        "status": "Pending",
        "class": "pacing",
    },
    {
        "id": 2,
        "title": "Research Paper",
        "subject": "History",
        "due": "05 Mar, 2026",
        "status": "Doing",
        "class": "doing",
    },
    {
        "id": 3,
        "title": "History Project",
        "subject": "Mavenatics",
        "due": "10 Mar, 2026",
        "status": "Completed",
        "class": "completed",
    },
    {
        "id": 4,
        "title": "Physics Lab Report",
        "subject": "Physics",
        "due": "12 Mar, 2026",
        "status": "Completed",
        "class": "completed",
    },
]


@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/forgot_password")
def forgot_password():
    return render_template("forgot_password.html")


@app.route("/reset_password")
def reset_password():
    return render_template("reset_password.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", tasks=tasks)


@app.route("/assignment")
def assignment():
    return render_template("assignment.html", tasks=tasks)


@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/edit_assignment/<int:id>")
def edit_assignment(id):
    return render_template("edit_assignment.html", id=id)


@app.route("/calender")
def calender():
    return render_template("calender.html")


@app.route("/subjects")
def subjects():
    return render_template("subjects.html")


@app.route("/grades")
def grades():
    return render_template("grades.html")


@app.route("/pomodoro")
def pomodoro():
    return render_template("pomodoro.html")


@app.route("/notes")
def notes():
    return render_template("notes.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/logout")
def logout():
    return render_template("logout.html")


if __name__ == "__main__":
    app.run(debug=True)
