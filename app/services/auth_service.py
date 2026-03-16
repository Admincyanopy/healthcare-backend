from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import RegisterUser
from fastapi import HTTPException
from app.utils.security import hash_password, verify_password


def register_user(db: Session, user: RegisterUser):

    existing_user = db.query(User).filter(
        User.phone_number == user.phone_number
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Phone already registered")

    hashed_password = hash_password(user.password)

    db_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        dob=user.dob,
        gender=user.gender,
        phone_number=user.phone_number,
        email=user.email,
        password=hashed_password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def login_user(db: Session, phone: str, password: str):

    user = db.query(User).filter(
        User.phone_number == phone
    ).first()

    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    return user