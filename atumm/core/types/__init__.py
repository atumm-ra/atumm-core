from abc import ABC, abstractmethod
from typing import Any, Optional, Type

from .presenters import AbstractPresenter
from .usecases import Command, CommandUseCase, Query, QueryUseCase
from .dataproviders import DataProvider


class AsyncContextManager(ABC):
    @abstractmethod
    async def __aenter__(self):
        pass

    @abstractmethod
    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Any,
    ) -> None:
        pass


class SyncContextManager(ABC):
    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Any,
    ) -> None:
        pass


__all__ = [
    "Command",
    "CommandUseCase",
    "Query",
    "QueryUseCase",
    "DataProvider",
    "AsyncContextManager",
    "SyncContextManager",
    "AbstractPresenter",
]
