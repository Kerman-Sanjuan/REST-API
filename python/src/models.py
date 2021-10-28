from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import Column, Integer, String
import db


class Master(db.Base):

    __tablename__ = 'Master'
    id_search = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)

    def __init__(self, PK_username):
        self.username = PK_username

    def __str__(self):
        return self.PK_username

    def getId(self):
        return self.id_search


class Details(db.Base):
    __tablename__ = 'Details'
    id_master = Column(Integer, ForeignKey(Master.id_search), primary_key=True)
    postal_code = Column(String)
    city = Column(String)

    def __init__(self, id_master, postal_code, city):
        self.postal_code = postal_code
        self.city = city
        self.id_master = id_master
