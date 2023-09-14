from sqlalchemy import Integer, String, ForeignKey, Boolean, Column
from sqlalchemy.orm import relationship

from .db import Base

import sqlalchemy

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)