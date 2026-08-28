from app.models.admin import Admin


def test_admin_model_has_required_columns_and_unique_email() -> None:
    table = Admin.__table__

    assert table.name == "admins"
    assert table.c.email.unique is True
    assert table.c.password_hash.nullable is False
    assert table.c.is_active.default.arg is True
    assert table.c.is_active.server_default is not None
