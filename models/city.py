#!/usr/bin/python3
""" City Module for HBNB project """
import os
from SQLAlchemy import Column, String, Foreignkey
from SQLAlchemy.orm import relationship
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(
            Strin(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    state_id = Column(
            Strin(60), Foreignkey('states.id'), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    places = relationship(
            'Place',
            cascade='all, delete, delete-orphan',
            backref='cities')
    if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
    state_id = ""
    name = ""
