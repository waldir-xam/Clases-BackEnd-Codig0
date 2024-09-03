from os import getenv
from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from config import environment
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(environment[getenv('ENVIRONMENT')])

api = Api(
    app,
    title="Boilerplate Flask",
    version='0.1',
    description='Endpoints del boilerplate',
    doc='/swagger-ui'
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
