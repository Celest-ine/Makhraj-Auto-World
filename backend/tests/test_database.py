from app.db.database import Base


def test_database_base_is_available_for_models() -> None:
    assert Base.metadata.tables == {}
