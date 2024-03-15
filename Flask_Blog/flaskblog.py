from flask import Flask, render_template, url_for

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)
