# Imports
import pytest
from pydantic import ValidationError

from assignment_1.config import Settings


def test_settings_read_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    """Read environment variables into typed settings"""
    monkeypatch.setenv("APP_NAME", "example-service")
    monkeypatch.setenv("APP_DEBUG", "true")
    settings = Settings(_env_file=None)
    assert settings.name == "example-service"
    assert settings.debug is True


def test_settings_reject_debug_in_production(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Reject debug mode in production"""
    monkeypatch.setenv("APP_ENVIRONMENT", "production")
    monkeypatch.setenv("APP_DEBUG", "true")
    with pytest.raises(ValidationError, match="APP_DEBUG must be false"):
        Settings(_env_file=None)
