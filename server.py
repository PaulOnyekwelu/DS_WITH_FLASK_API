from sqlite3 import Connection as SQLite3Connection
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
import linked_list


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


# instantiating db
db = SQLAlchemy(app)
now = datetime.now()

# models
class User(db.Model):
    """a user table model for our database"""

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    posts = db.relationship("BlogPost")


class BlogPost(db.Model):
    """blog_post model for our database"""

    __tablename__ = "blog_post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.String(300))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


# app routes
@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    if (
        not data["name"]
        or not data["email"]
        or not data["address"]
        or not data["phone"]
    ):
        return jsonify({"message": "Please provide all fields"}), 400
    user = User.query.filter_by(email=data["email"]).first()
    if user:
        return jsonify({"message": "Email already taken"}), 400
    new_user = User(
        name=data["name"],
        email=data["email"],
        address=data["address"],
        phone=data["phone"],
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(data), 201


@app.route("/user/descending_id", methods=["GET"])
def get_all_users_descending():
    users = User.query.all()
    user_ll = linked_list.LinkedList()
    for user in users:
        user_ll.insert_beginning(
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "address": user.address,
                "phone": user.phone,
            }
        )
    users = user_ll.to_list()
    return jsonify(users), 200


@app.route("/user/ascending_id", methods=["GET"])
def get_all_users_ascending():
    users = User.query.all()
    user_ll = linked_list.LinkedList()
    for user in users:
        user_ll.insert_end(
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "address": user.address,
                "phone": user.phone,
            }
        )
    users = user_ll.to_list()
    return jsonify(users), 200


@app.route("/user/<user_id>", methods=["GET"])
def get_user(user_id):
    users = User.query.all()
    user_ll = linked_list.LinkedList()
    for user in users:
        user_ll.insert_beginning(
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "address": user.address,
                "phone": user.phone,
            }
        )

    user = user_ll.get_user_by_id(user_id)
    return jsonify(user), 200


@app.route("/user/<user_id>", methods=["DELETE"])
def delete_user():
    pass


@app.route("/user/<user_id>", methods=["GET"])
def get_all_blog_posts():
    pass


@app.route("/blog_post/<user_id>", methods=["POST"])
def create_blog_post():
    pass


@app.route("/b log_post/<blog_id>", methods=["GET"])
def get_blog_post():
    pass


@app.route("/blog_post/<blog_id>", methods=["DELETE"])
def delete_blog_post():
    pass


if __name__ == "__main__":
    print(__name__)
    app.run(debug=True)
