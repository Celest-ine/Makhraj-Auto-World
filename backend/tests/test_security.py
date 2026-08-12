import pytest

from app.core.security import hash_password, verify_password


def test_password_hash_is_not_plaintext_and_verifies() -> None:
    password = "correct horse battery staple"

    password_hash = hash_password(password)

    assert password_hash != password
    assert password_hash.startswith("$argon2id$")
    assert verify_password(password, password_hash) is True
    assert verify_password("incorrect password", password_hash) is False


def test_password_hashing_rejects_empty_password() -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        hash_password("")


def test_invalid_stored_hash_is_rejected_without_an_internal_error() -> None:
    assert verify_password("any password", "not-a-valid-password-hash") is False
