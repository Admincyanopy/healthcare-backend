from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    bcrypt__rounds=12,
    deprecated="auto"
)


def hash_password(password: str) -> str:
    try:
        # ✅ bcrypt limit fix
        password = password[:72]
        return pwd_context.hash(password)
    except Exception as e:
        print("HASH ERROR:", e)
        raise


def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        # ✅ bcrypt limit fix
        plain_password = plain_password[:72]
        return pwd_context.verify(plain_password, hashed_password)
    except Exception as e:
        print("VERIFY ERROR:", e)
        return False  # ✅ prevent server crash