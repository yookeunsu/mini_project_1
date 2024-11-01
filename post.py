from flask import *

post_bp = Blueprint('post', __name__)

@post_bp.route('/post')
def post():
    return render_template('post/post.html')