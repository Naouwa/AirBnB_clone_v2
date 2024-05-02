#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """ Review classto store review information """
    if models.storage_t == "db":
        __tablename__ = "reviews"
        place_id = Column(String(128), ForeignKey("place.id"), nullable=False)
        user_id = Column(String(128), ForeignKey("users.id"), nullable=False)
        text = Column(String(128), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """Review's initialization"""
        super().__init__(*args, **kwargs)
