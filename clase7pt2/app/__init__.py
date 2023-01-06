from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

api = Api(
    app,
    title='Boilerplate Flask',
    version='0.1',
    description='Endpoints del boilerplate',
    doc='/swagger-ui'
)

db = SQLAlchemy(app)
