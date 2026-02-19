from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, User, Assignment
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User(username=username)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password")

    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/dashboard")
@login_required
def dashboard():
    assignments = Assignment.query.filter_by(user_id=current_user.id).all()
    return render_template("dashboard.html", assignments=assignments)

@app.route("/add", methods=["GET","POST"])
@login_required
def add_assignment():
    if request.method == "POST":
        title = request.form["title"]
        subject = request.form["subject"]
        due_date = datetime.strptime(request.form["due_date"], "%Y-%m-%d")

        new_assignment = Assignment(
            title=title,
            subject=subject,
            due_date=due_date,
            user_id=current_user.id
        )

        db.session.add(new_assignment)
        db.session.commit()
        return redirect(url_for("dashboard"))

    return render_template("add_assignment.html")

@app.route("/calendar")
@login_required
def calendar():
    assignments = Assignment.query.filter_by(user_id=current_user.id).all()
    return render_template("calendar.html", assignments=assignments)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)