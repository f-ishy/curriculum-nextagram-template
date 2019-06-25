from flask import Flask, render_template, request, redirect, url_for, Blueprint, flash
from models.following import Following
from models.user import User
# from models.user import User
from flask_login import current_user

following_blueprint = Blueprint('following',
                            __name__,
                            template_folder='templates')

@following_blueprint.route('/follow/<id>', methods=['POST'])
def create(id):
    user = User.get_or_none(User.id == id)
    follow = Following.get_or_create(
        user_id=id,
        follower_id=current_user.id
        )
    follow[0].approved = True
    follow[0].save()
    # follow is a tuple of (Following object, boolean if a new Following object is created)
    # More info here http://docs.peewee-orm.com/en/latest/peewee/api.html#Model.get_or_create 
    return redirect(url_for('users.show', username = user.username))

@following_blueprint.route('/unfollow/<id>', methods=['POST'])
def destroy(id):
    # user = User.get_or_none(User.id == id)
    f = Following.get_or_none((Following.user_id==id) & (Following.follower_id==current_user.id))
    f.delete_instance()
    return redirect(url_for('users.show', username = user.username))
