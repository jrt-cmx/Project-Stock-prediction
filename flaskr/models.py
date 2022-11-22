# models.py: Contains models for database tables

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Search(db.Model):
    __tablename__ = 'search'
    row_id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.Integer, nullable=False)
    search_term = db.Column(db.String(), nullable=False)

