#!/usr/bin/python3
"""review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class"""
    place_id = ""
    usser_id = ""
    text = ""
