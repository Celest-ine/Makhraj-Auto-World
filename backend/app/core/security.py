from argon2 import PasswordHasher, Type
from argon2.exceptions import InvalidHashError, VerificationError

_password_hasher = PasswordHasher(type=Type.ID)


def hash_password(password: str) -> str:
    """Create an Argon2id password hash; never persist the plaintext password."""
    if not password:
        raise ValueError("Password must not be empty.")
    return _password_hasher.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    """Safely verify a plaintext password against its stored hash."""
    try:
        return _password_hasher.verify(password_hash, password)
    except (InvalidHashError, VerificationError):
        return False
