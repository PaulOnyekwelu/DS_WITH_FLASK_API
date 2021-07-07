from flask import Flask
from sqlite3 import Connection as SQLite3Connection
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0


# configure sqlite3 to enforce foreign key constraints
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_key=ON;")
        cursor.close()


