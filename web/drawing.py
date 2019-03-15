from flask import (Blueprint, render_template, redirect, request, url_for)
from web.kanjidb import get_db

bp = Blueprint('draw', __name__)

@bp.route('/', methods=['GET', 'POST'])
def canvas(kanji="愛"):
    if request.method == 'POST':
        kanjitext = request.form['kanjitext']
        kanji=kanjitext[:1]
    return render_template('canvas.html',kanji=kanji)

@bp.route('/save', methods=['POST'])
def save():
    kanji=request.form['kanji']
    jsondata = request.form['jsondata']
    db = get_db()
    db.execute(
    "INSERT INTO kanjis (kanji, jsondata) VALUES (?, ?)",
    (kanji, jsondata)
    )
    db.commit()  
    return redirect(url_for('draw.canvas', kanji=kanji))

@bp.route('/kreader', methods=['GET'])
def readingtest():
    db=get_db()
    testdata = db.execute('SELECT * FROM kanjis').fetchone()
    return render_template('kanjireader.html', data=testdata)