#!/usr/bin/python3
"""
review module
"""


from .base_model import BaseModel


class Review(BaseModel):
    """Review class"""
    place_id: str = ""
    user_id: str = ""
    text: str = ""
