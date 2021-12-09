#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Dict

class BasePostgresql(ABC):
    
    @abstractmethod
    def config_parser_params() -> Dict:
        ...
        
    @abstractmethod
    def connect():
        ...

    @abstractmethod
    def close():
        ...