from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "TEST_SECRET"

posts = [
    {
        "author": "SwamFire",
        "title": "Blog Post 1",
        "content": "First Post Content",
        "date_posted": "Today",
    },
    {
        "author": "SwamFire 2",
        "title": "Blog Post 2",
        "content": "First Post Content 2",
        "date_posted": "Today after 5 Minutes",
    },
]


@app.route("/")
@app.route("/home")
def home():
    # return "<h1>Hello, World!</h1>"
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    # return "<h1>About Page</h1>"
    return render_template("about.html", title="About")


@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash(f"You have been logged in Successfully!", "success")
            return redirect(url_for("home"))
        else:
            flash(f"Login Unsuccessful. Please ID or Password", "danger")
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
