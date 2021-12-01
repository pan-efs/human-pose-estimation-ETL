#!/usr/bin/python
import psycopg2

from utils.config import Config
from base.base_class import BasePostgresql

class Connect(BasePostgresql):
    def __init__(self, 
            filename: str, 
            section: str
        ):
        self.filename = filename
        self.section = section
        self.conn = None
        self.connect()
    
    
    def config_parser_params(self):
        return Config(self.filename, self.section).config_parser()
    

    def close(self):
        if self.conn is not None:
            self.conn.close()
            print("Database connection closed.")
    

    def connect(self):

        try:
            params = self.config_parser_params()

            print("Connecting to DB...")
            self.conn = psycopg2.connect(**params)

            cursor = self.conn.cursor()
            
            print("PostgreSQL database version:")
            cursor.execute("SELECT version()")

            db_version = cursor.fetchone()
            print(db_version)

            cursor.close()

            return 1
        
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)
        
        finally:
            self.close()
