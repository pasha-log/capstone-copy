"""SQLAlchemy models for Carbon Print Calculator."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 

class User(db.Model):
    """User in the system."""

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    username = db.Column(
        db.String(70),
        nullable=False,
        unique=True,
    )

    password = db.Column(
        db.Text,
        nullable=False,
    )

    email = db.Column(
        db.String(120),
        nullable=False,
        unique=True,
    )

    def __repr__(self):
        return f"<User #{self.id}: {self.username}, {self.email}>"

def connect_db(app): 
    db.app = app 
    db.init_app(app)

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)