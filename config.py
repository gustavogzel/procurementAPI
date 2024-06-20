# config.py

import pathlib
import connexion
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

ip_databse = os.environ['IP_DB']



basedir = pathlib.Path(__file__).parent.resolve()
connex_app = connexion.App(__name__, specification_dir=basedir)

app = connex_app.app
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://pstguser:pstg123@'+ip_databse+'/contrataciones'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
CORS(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

