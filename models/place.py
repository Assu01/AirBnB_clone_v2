#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base, Column, String
from models.base_model import Integer, ForeignKey
from sqlalchemy import Float, Table
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place"""

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    reviews = relationship('Review', back_populates='place', cascade='delete')
    user = relationship(
        'User', back_populates='places')
    amenities = relationship('Amenity', secondary=place_amenity,
                             viewonly=False, back_populates='place_amenities')
