import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
     # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    name = Column(String(30), nullable=False)
    lastname = Column(String(30))    
    email = Column(String(30), nullable=False)

class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    population = Column(Integer, nullable=False)
    terrain = Column(String(30), nullable=False)

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    gender = Column(String(30), nullable=False)
    hair_color = Column(String(30), nullable=False)
    eye_color = Column(String(30), nullable=False)  

class Favorite(Base):
    __tablename__ = 'favorites'   
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')