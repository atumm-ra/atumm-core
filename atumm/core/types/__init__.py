from abc import ABC, abstractmethod
from typing import Optional, Type, Any
from .usecases import Command, CommandUseCase, Query, QueryUseCase
from .presenters import AbstractPresenter

__all__ = ['Command', 'CommandUseCase', 'Query', 'QueryUseCase', 'AsyncContextManager', 'SyncContextManager', 'AbstractPresenter']


class AsyncContextManager(ABC):

    @abstractmethod
    async def __aenter__(self): pass
    
    @abstractmethod
    async def __aexit__(self, exc_type: Optional[Type[BaseException]], exc_value: Optional[BaseException], traceback: Any) -> None: pass
    
    @classmethod
    def __subclasshook__(cls, C):
        if cls is AbstractAsyncContextManager:
            return _collections_abc._check_methods(C, "__aenter__",
                                                   "__aexit__")
        return NotImplemented


class SyncContextManager(ABC):

    @abstractmethod
    def __enter__(self): pass

    @abstractmethod
    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_value: Optional[BaseException], traceback: Any) -> None: pass

