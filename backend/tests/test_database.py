from app.db.database import Base
from app.models.admin import Admin


def test_database_base_registers_models() -> None:
    assert Base.metadata.tables["admins"] is Admin.__table__
