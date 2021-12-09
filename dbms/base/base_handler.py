#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, Optional


"""
Chain of Responsibility as Design Pattern.
"""

class BaseHandler(ABC):
    """
    A Handler interface which declares a method for building the chain of handlers
    and a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: 'BaseHandler') -> 'BaseHandler':
        return handler
    

    @abstractmethod
    def handle(self, req) -> Optional[str]:
        ...


class AbstractBaseHandler(BaseHandler):
    """
    The default chaining behavior.
    """

    _next: BaseHandler = None

    def set_next(self, handler: BaseHandler) -> BaseHandler:
        self._next = handler
        return self._next
    

    @abstractmethod
    def handle(self, req: Any) -> str:
        return self._next.handle(req) if self._next else None
