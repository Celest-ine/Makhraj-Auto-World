from pathlib import Path

from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine, inspect

from app.core.config import get_settings


def test_admin_migration_creates_admins_table(tmp_path: Path, monkeypatch) -> None:
    database_url = f"sqlite+pysqlite:///{(tmp_path / 'migration-test.db').as_posix()}"
    monkeypatch.setenv("DATABASE_URL", database_url)
    monkeypatch.setenv("SECRET_KEY", "migration-test-secret")
    get_settings.cache_clear()

    try:
        config = Config(str(Path(__file__).parents[1] / "alembic.ini"))
        config.set_main_option("sqlalchemy.url", database_url)
        command.upgrade(config, "head")

        inspector = inspect(create_engine(database_url))
        assert inspector.has_table("admins")
        assert {column["name"] for column in inspector.get_columns("admins")} == {
            "id",
            "email",
            "password_hash",
            "is_active",
            "created_at",
            "updated_at",
        }
    finally:
        get_settings.cache_clear()
