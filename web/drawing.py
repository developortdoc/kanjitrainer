from flask import (Blueprint, render_template, redirect, request, url_for)

bp = Blueprint('draw', __name__)

@bp.route('/', methods=['GET', 'POST'])
def canvas(kanji="愛"):
    if request.method == 'POST':
        kanjitext = request.form['kanjitext']
        kanji=kanjitext[:1]
    return render_template('canvas.html',kanji=kanji)

@bp.route('/save', methods=['POST'])
def save(kanji):
    return redirect(url_for('drawing.canvas', kanji=kanji))