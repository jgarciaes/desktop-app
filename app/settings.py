import os
from dataclasses import dataclass


@dataclass
class Settings:
    desktop_version: str = os.getenv("DESKTOP_VERSION", "dev")
    otel_exporter_otlp_endpoint: str = os.getenv(
        "OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4318/v1/traces"
    )


settings = Settings()
