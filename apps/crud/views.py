from flask import Blueprint, render_template, redirect, url_for
from apps.app import db
from apps.crud.models import User
from apps.crud.forms import Userform


crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)

@crud.route("/")
def index():
    return render_template("crud/index.html")

@crud.route("/sql")
def sql():
    db.session.query(User).all()
    return "콘솔 로그를 확인해주세요"

@crud.route("/toons/new", methods=["GET", "POST"])
def create_toon():
    form = Userform()

    if form.validate_on_submit():
        toon = User(
            title = form.title.data,
            author = form.author.data,
            genre = form.genre.data,
            link = form.link.data,
        )
        db.session.add(toon)
        db.session.commit()

        return redirect(url_for("crud.toons"))
    
    return render_template("crud/create.html", form=form)

@crud.route("/toons")
def toons():

    toons = User.query.all()
    return render_template("crud/index.html", toons=toons)