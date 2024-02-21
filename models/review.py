#!/usr/bin/python3
""" City Module for HBNB project """

from SQLAlchemy import Column, String, ForeignKey
from SQLAlchemy.orm import relationship
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'reviews'
    text = Column(Strin(1024), nullable=False)
    place_id = Column(Strin(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(Strin(60), ForeignKey("places.id"), nullable=False)
