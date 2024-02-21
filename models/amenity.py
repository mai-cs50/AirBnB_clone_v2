#!/usr/bin/python3
""" City Module for HBNB project """

from SQLAlchemy import Column, String, ForeignKey
from SQLAlchemy.orm import relationship
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'amenities'
    name = Column(Strin(12/), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
