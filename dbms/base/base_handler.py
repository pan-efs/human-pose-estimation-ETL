#!/usr/bin/python
from abc import ABC, abstractmethod
from typing import Any, Optional


class BaseHandler(ABC):

    @abstractmethod
    def set_next(self, handler: 'BaseHandler') -> 'BaseHandler':
        return handler
    

    @abstractmethod
    def handle(self, req) -> Optional[str]:
        ...


class AbstractBaseHandler(BaseHandler):

    _next: BaseHandler = None

    def set_next(self, handler: BaseHandler) -> BaseHandler:
        self._next = handler
        return self._next
    

    @abstractmethod
    def handle(self, req: Any) -> str:
        return self._next.handle(req) if self._next else None
