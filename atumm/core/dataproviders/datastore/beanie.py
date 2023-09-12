from abc import ABC
from typing import Generic, TypeVar

from atumm.core.dataproviders import DataProvider
from beanie import Document

DocumentType = TypeVar("DocumentType", bound=Document)


class BeanieDataProvider(DataProvider, Generic[DocumentType]):
    pass
