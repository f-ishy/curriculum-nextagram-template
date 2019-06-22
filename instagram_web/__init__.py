from app import app
from flask import render_template
from instagram_web.blueprints.users.views import users_blueprint
from instagram_web.blueprints.posts.views import posts_blueprint
from instagram_web.blueprints.following.views import following_blueprint
from instagram_web.blueprints.donate.views import donate_blueprint
from flask_assets import Environment, Bundle
from .util.assets import bundles
from instagram_web.util.google_oauth import oauth

assets = Environment(app)
assets.register(bundles)

app.register_blueprint(users_blueprint, url_prefix="/users")
app.register_blueprint(posts_blueprint, url_prefix="/posts")
app.register_blueprint(following_blueprint, url_prefix="/following")
app.register_blueprint(donate_blueprint, url_prefix="/donate")

oauth.init_app(app)

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route("/")
def home():
    return render_template('home.html')
