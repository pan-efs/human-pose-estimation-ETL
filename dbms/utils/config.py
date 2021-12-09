from configparser import ConfigParser
from typing import Dict

class Config:
    """
    A parser class of configuration file.
    """

    def __init__(self, filename: str, section: str):
        self.filename = filename
        self.section = section


    def config_parser(self) -> Dict:
        parser = ConfigParser()
        parser.read(self.filename)

        db = {}
        
        if parser.has_section(self.section):
            params = parser.items(self.section)
            for p in params:
                db[p[0]] = p[1]
        
        else:
            raise Exception('Section {0} not found in the {1} file'.format(self.section, self.filename))
        
        return db