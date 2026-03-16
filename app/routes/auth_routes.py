from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import random

from app.database import get_db
from app.schemas.user_schema import RegisterUser, LoginUser
from app.services.auth_service import register_user, login_user

router = APIRouter()

otp_store = {}


# SEND OTP
@router.post("/send-otp")
def send_otp(phone_number: str):

    otp = str(random.randint(100000, 999999))
    otp_store[phone_number] = otp

    print("OTP sent to", phone_number, ":", otp)

    return {"message": "OTP sent successfully"}


# VERIFY OTP
@router.post("/verify-otp")
def verify_otp(phone_number: str, otp: str):

    saved_otp = otp_store.get(phone_number)

    if not saved_otp:
        raise HTTPException(status_code=400, detail="OTP not found")

    if saved_otp != otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    del otp_store[phone_number]

    return {"message": "OTP verified"}


# REGISTER USER
@router.post("/register")
def register(user: RegisterUser, db: Session = Depends(get_db)):

    new_user = register_user(db, user)

    return {
        "message": "User registered successfully",
        "user_id": new_user.id
    }


# LOGIN USER
@router.post("/login")
def login(user: LoginUser, db: Session = Depends(get_db)):

    db_user = login_user(db, user.phone_number, user.password)

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "message": "Login successful",
        "user_id": db_user.id
    }