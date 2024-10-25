from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from api.models import db
from api.routes import api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db.init_app(app)  # Initialize SQLAlchemy with app
migrate = Migrate(app, db)  # Initialize Flask-Migrate with app and db

# Register the Blueprint
app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
