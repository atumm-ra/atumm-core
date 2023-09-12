from typing import Dict, List, Optional, Tuple

from atumm.core.exceptions import RuntimeException
from pydantic import BaseModel


class ExceptionDetailResponse(BaseModel):
    type: str
    reason: str
    metadata: Optional[Dict[str, str]]


class RuntimeExceptionResponse(BaseModel):
    code: int
    message: str
    status: str
    details: Optional[List[ExceptionDetailResponse]]


def map_exception_to_response(
    exception: RuntimeException,
) -> Tuple[int, RuntimeExceptionResponse]:
    response = RuntimeExceptionResponse(**exception.dict())
    return response.code, response
