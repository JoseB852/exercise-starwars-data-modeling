import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False, unique=True)
    firstname = Column (String(250), nullable=False)
    lastname = Column(String(250), nullable=False)

class Planets (Base):
    __tablename__ = 'plantes'
    id = Column(Integer, primary_key=True)
    name = Column (String(250), nullable=False, unique=True)


class Films (Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    name = Column(String(100),nullable=False)
    year = Column(Integer,nullable=False,unique=True)
    director = Column(String(50),nullable=False)

class Characters (Base):
    __tablename__ = 'charcaters'
    id = Column (Integer, primary_key=True)
    name = Column (String (250),nullable=False, unique=True)
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    homeworld = relationship(Planets)
    films_id = Column(Integer,ForeignKey('films.id'))
    films = relationship(Films)

class Favorite_Plantes (Base):
    __tablename__ ='favorites_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    users = relationship(User)
    planets_id = Column(Integer, ForeignKey('plantes.id'))
    planets = relationship(Planets)

class Characters_Films (Base):
    __tablename__ = 'characters_films'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    character =relationship(Characters)
    films_id = Column(Integer, ForeignKey('films.id'))
    films = relationship(Films)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
