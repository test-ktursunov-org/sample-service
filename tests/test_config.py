import pytest

from sample_service.config import Settings


def test_the_defaults_bind_to_loopback():
    settings = Settings.from_env({})

    assert settings.host == "127.0.0.1"
    assert settings.port == 8080


@pytest.mark.parametrize("value", ["INFO", "Info", "info"])
def test_the_log_level_is_normalised(value):
    assert Settings.from_env({"SERVICE_LOG_LEVEL": value}).log_level == "info"
