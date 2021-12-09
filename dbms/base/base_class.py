#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Dict

class BasePostgresql(ABC):
    
    @abstractmethod
    def config_parser_params() -> Dict:
        """
        A method which parses configuration's parameters.

        Returns: Dict
        """
        ...
        
    @abstractmethod
    def connect():
        """
        A method which connects with the database.
        """
        ...

    @abstractmethod
    def close():
        """
        A method which closes the connection with the database.
        """
        ...