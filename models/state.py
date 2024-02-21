#!/usr/bin/python3
""" City Module for HBNB project """
import os
from SQLAlchemy import Column, String
from SQLAlchemy.orm import relationship
from models.base_model import BaseModel, Base
from mdels.city import City
import models

class State(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'states'
    name = Column(Strin(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """    """
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
