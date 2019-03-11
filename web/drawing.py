from flask import (Blueprint, render_template, request)

bp = Blueprint('draw', __name__)

@bp.route('/', methods=['GET', 'POST'])
def canvas():
    return render_template('canvas.html')