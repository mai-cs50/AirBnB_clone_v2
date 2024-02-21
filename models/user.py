#!/usr/bin/python3
""" City Module for HBNB project """

from SQLAlchemy import Column, String
from SQLAlchemy.orm import relationship
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'users'
    email = Column(Strin(128), nullable=False)
    password = relationship("City", backref="state", cascade="delete")
    first_name = Column(Strin(128))
    last_name = Column(Strin(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Place", backref="user", cascade="delete")
