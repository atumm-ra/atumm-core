from __future__ import annotations

from collections import UserDict
from typing import Any

from pydantic import BaseSettings


class Config(BaseSettings):
    @classmethod
    def create_from_env_file(cls, filename: str = ".env") -> Config:
        return cls(_env_file=filename)


class Configure:
    configurations = UserDict()

    def build_configuration_class(self) -> Config:
        annotations = {}
        defaults = {}
        for config_cls in self.configurations.values():
            for field_name, field_definition in config_cls.__fields__.items():
                annotations[field_name] = field_definition.outer_type_
                if field_definition.default != field_definition.default_factory:
                    defaults[field_name] = field_definition.default

        MergedConfigAttributes = {"__annotations__": annotations, **defaults}

        MergedConfig = type("MergedConfig", (Config,), MergedConfigAttributes)
        return MergedConfig

    def build(self, env_file: str = ".env") -> Config:
        MergedConfig = self.build_configuration_class()
        return MergedConfig.create_from_env_file(env_file)

    def __call__(self, cls) -> None:
        if not issubclass(cls, Config):
            raise TypeError(
                f"{cls.__name__} is not of type {Config.__class__.__name__}"
            )
        self.configurations[cls.__name__] = cls


configure = Configure()
