from flask import render_template, url_for, session, redirect
from flask.ext.login import current_user
from .. import db
from ..models import User, Permission, Post
from . import main
from .forms import NameForm, PostForm

@main.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if current_user.can(Permission.WRITE_ARTICLE) and \
        form.validate_on_submit():
        post = Post(body=form.body.data,
                     author = current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('main.index'))
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', form=form, posts=posts)