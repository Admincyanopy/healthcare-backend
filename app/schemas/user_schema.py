from pydantic import BaseModel


class RegisterUser(BaseModel):
    first_name: str
    last_name: str
    dob: str
    gender: str
    phone_number: str
    email: str
    password: str


class LoginUser(BaseModel):
    phone_number: str
    password: str