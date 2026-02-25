from flask import Flask, render_template, request, redirect, url_for, session
from flask import flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "secret123"

DATABASE = "assignments.db"


def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    c.execute(
        """
        CREATE TABLE IF NOT EXISTS assignments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            subject TEXT NOT NULL,
            due_date TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """
    )

    conn.commit()
    conn.close()


init_db()


@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")

        session["user"] = email
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

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    c.execute("SELECT * FROM assignments")
    assignments = c.fetchall()

    c.execute("SELECT COUNT(*) FROM assignments")
    total = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM assignments WHERE status='Pending'")
    pending = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM assignments WHERE status='Doing'")
    doing = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM assignments WHERE status='Completed'")
    completed = c.fetchone()[0]

    conn.close()

    return render_template(
        "dashboard.html",
        user=session["user"],
        assignments=assignments,
        total=total,
        pending=pending,
        doing=doing,
        completed=completed,
    )


@app.route("/add", methods=["GET", "POST"])
def add():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        title = request.form["title"]
        subject = request.form["subject"]
        due_date = request.form["due_date"]
        status = request.form["status"]

        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute(
            """
            INSERT INTO assignments (title, subject, due_date, status)
            VALUES (?, ?, ?, ?)
        """,
            (title, subject, due_date, status),
        )
        conn.commit()
        conn.close()

        return redirect(url_for("dashboard"))

    return render_template("add_assignment.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if "user" not in session:
        return redirect(url_for("login"))

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    if request.method == "POST":
        title = request.form["title"]
        subject = request.form["subject"]
        due_date = request.form["due_date"]
        status = request.form["status"]

        c.execute(
            """
            UPDATE assignments
            SET title=?, subject=?, due_date=?, status=?
            WHERE id=?
        """,
            (title, subject, due_date, status, id),
        )

        conn.commit()
        conn.close()
        return redirect(url_for("dashboard"))

    c.execute("SELECT * FROM assignments WHERE id=?", (id,))
    assignment = c.fetchone()
    conn.close()

    return render_template("edit_assignment.html", assignment=assignment)


@app.route("/delete/<int:id>")
def delete(id):
    if "user" not in session:
        return redirect(url_for("login"))

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("DELETE FROM assignments WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect(url_for("dashboard"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
