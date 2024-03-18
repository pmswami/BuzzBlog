from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get("page", 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=3, page=page)
    return render_template("home.html", posts=posts)


@main.route("/about")
def about():
    # return "<h1>About Page</h1>"
    return render_template("about.html", title="About")
