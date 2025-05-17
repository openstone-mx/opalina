import os
import datetime as dt
from typing import Optional
from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class CLI:
    now: dt.datetime = field(default_factory=dt.datetime.utcnow)
    version: Optional[str] = None

    @classmethod
    def _auto(cls):
        from opalina.version import version

        # Auto configure CLI instance
        return cls(version=version)

    @classmethod
    def cli_exec(cls):
        import fire

        # Create CLI instance with default values
        cli = cls._auto()
        return fire.Fire(cli)

    def environ(self, name: str) -> Optional[str]:
        return os.environ.get(name)

    def hello(self, name: Optional[str] = None) -> str:
        name = name or self.environ(name="OPA_TARGET_NAME") or "World"
        return f"Hello, {name}!"
