from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app() -> Flask:
    # Creates and configures the app.
    basedir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    app = Flask (
        __name__,
        # These two are not necesarry, but are great to have, because otherwise, the folder with html files and resources for html,
        # would end up in the app folder. Remember to actually make the folders too.
        template_folder=os.path.join(basedir, "html"),
        static_folder=os.path.join(basedir, "resources")
    )

    # Global config.
    app.config.from_mapping(
        # The key for encryption.
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        SQLALCHEMY_DATABASE_URI = 'sqlite:///{basedir}/{database}'.format(
                basedir=basedir, database="database.db"
            ),
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

    # Initialisere SQLAlchemy.
    # We will save cat pictures here.
    db.init_app(app)



    ## Indlæser alle tabeller brugt i databasen
    # from app.auth import models
    # from app.api import models

    # Creates the database and tables.
    with app.app_context():
        db.create_all()

    
    from flaskr.addresses import bp as main_bp
    app.register_blueprint(main_bp)

    return app