#!/usr/bin/env python3
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from utils.config import Config
from base.base_class import BasePostgresql

class DataBase(BasePostgresql):

    def __init__(self, 
            filename: str, 
            section: str
        ):
        self.filename = filename
        self.section = section
        self.conn = None
        self.params = self.config_parser_params()
    

    def config_parser_params(self):
        return Config(self.filename, self.section).config_parser()
    

    def close(self):
        if self.conn is not None:
            self.conn.close()
            print("DBMS connection closed.")
    
    
    def connect(self):
        try:
            print("Connecting to DBMS...")
            return psycopg2.connect(**self.params)

        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
    

    def create_database(self, 
            command: str,  
        ):
        try:
            if "CREATE DATABASE" not in command.upper():
                raise SyntaxError("No CREATE DATABASE command found!")

            self.conn = self.connect()
            self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    
            cursor = self.conn.cursor()
    
            cursor.execute(command)
            print("Database has been created successfully!")

        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
        
        finally:
            self.close()
    

    def drop_database(self, 
            command: str,  
        ):
        try:
            if "DROP DATABASE" not in command.upper():
                raise SyntaxError("No DROP DATABASE command found!")

            self.conn = self.connect()
            self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    
            cursor = self.conn.cursor()
    
            cursor.execute(command)
            print("Database has been dropped successfully!")

        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
        
        finally:
            self.close()
