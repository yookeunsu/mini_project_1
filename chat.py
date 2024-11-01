from flask import *

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat')
def chat():
    return render_template('chat/chat.html')