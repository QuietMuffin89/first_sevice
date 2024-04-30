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

@crud.route("/users/new", methods=["GET", "POST"])
def create_user():
    form = Userform()

    if form.validate_on_submit():
        user = User(
            title = form.title.data,
            author = form.author.data,
            genre = form.genre.data,
            link = form.link.data,
        )
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("crud.users"))
    
    return render_template("crud/create.html", form=form)

@crud.route("/users")
def users():

    users = User.query.all()
    return render_template("crud/index.html", users=users)

@crud.route("/users/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    form = Userform()

    user = User.query.filter_by(id=user_id).first()

    if form.validate_on_submit():
        # user.id = form.id.data
        user.title = form.title.data
        user.author = form.autor.data
        user.genre = form.genre.data
        user.link = form.link.data

        db.session.add(user)
        db.session.commit()
        return redirect(url_for("crud.users"))
    
    return render_template("crud/edit.html", user=user, form=form)

@crud.route("/users/<user_id>/delete", methods=["POST"])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("crud.users"))
