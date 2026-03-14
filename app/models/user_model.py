from sqlalchemy import Column, Integer, String
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String)
    last_name = Column(String)
    dob = Column(String)
    gender = Column(String)

    phone_number = Column(String, unique=True, index=True)
    email = Column(String, unique=True)

    password = Column(String)