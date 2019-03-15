from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    
    from . import drawing
    app.register_blueprint(drawing.bp)

    app.config.from_mapping(
            SECRET_KEY='temp',
            DATABASE=os.path.join(app.instance_path, 'kanjidb.sqlite3'),
        )

    from . import kanjidb
    kanjidb.init_app(app)

    return app
