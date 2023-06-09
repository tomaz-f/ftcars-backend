from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def config_database(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://admin:admin@postgresql:5432/cars'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()
