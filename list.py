from flask import *

list_bp = Blueprint('list', __name__)

@list_bp.route('/list')
def list():
    return render_template('list/list.html')