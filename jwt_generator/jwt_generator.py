import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your-secret-key"


def generate_jwt(data):
    payload = {
        "exp": datetime.utcnow() + timedelta(hours=1),
        "iat": datetime.utcnow(),
        "sub": data,
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
