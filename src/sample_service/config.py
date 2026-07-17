import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    host: str
    port: int
    log_level: str

    @classmethod
    def from_env(cls, env: dict[str, str] | None = None) -> "Settings":
        source = os.environ if env is None else env
        return cls(
            host=source.get("SERVICE_HOST", "127.0.0.1"),
            port=int(source.get("SERVICE_PORT", "8080")),
            log_level=source.get("SERVICE_LOG_LEVEL", "info").lower(),
        )
