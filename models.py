import datetime

from sqlalchemy import create_engine, text
from sqlalchemy import (Column, Integer, String, DateTime,
                        Boolean, Text, DECIMAL, ForeignKey)
from sqlalchemy.orm import (scoped_session, sessionmaker,
                            relationship, backref)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import postgresql
from geoalchemy2 import Geometry


Base = declarative_base()

def init_db(engine):
  Base.metadata.create_all(bind=engine)


class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    routes = relationship("Route")


class Route(Base):
    __tablename__ = "route"
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("author.id", ondelete="SET NULL"),
                       nullable=True)
    uuid = Column(
        postgresql.UUID, unique=True,
        server_default=text("uuid_generate_v4()"),
        index=True
    )
    geom = Column(Geometry("MULTILINESTRING"))
    name = Column(String)
    description = Column(String)

    # AVG metrics
    difficulty = Column(DECIMAL(10,2), default=0.0)
    ground = Column(DECIMAL(10,2), default=0.0)
    air = Column(DECIMAL(10,2), default=0.0)
    landscape = Column(DECIMAL(10,2), default=0.0)
    condition = Column(DECIMAL(10,2), default=0.0)
    technique = Column(DECIMAL(10,2), default=0.0)
    fun_factor = Column(DECIMAL(10,2), default=0.0)
    track_description = Column(DECIMAL(10,2), default=0.0)

    distance = Column(Integer)
    date = Column(DateTime(timezone=True), index=True)
    created = Column(DateTime(timezone=True), index=True)
    modified = Column(DateTime(timezone=True), index=True,
                      default=datetime.datetime.now())
    elevation = Column(postgresql.ARRAY(Integer))
    file = Column(String(255))


