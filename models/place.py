#!/usr/bin/python3
"""
Place module
"""
from .base_model import BaseModel


class Place(BaseModel):
    """
    Place class
    """
    city_id: str = ""
    user_id: str = ""
    name = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: list = []
