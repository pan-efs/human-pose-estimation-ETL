#!/usr/bin/env python3
import psycopg2
from psycopg2.extras import DictCursor

from utils.config import Config
from base.base_class import BasePostgresql


class Tables(BasePostgresql):

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
    

    def connect(self):
        try:
            print("Connecting to DB...")
            return psycopg2.connect(**self.params)

        except (Exception, psycopg2.DatabaseError) as e:
            print(e)


    def close(self):
        if self.conn is not None:
            self.conn.close()

    
    def create_table(self, 
            command: str, 
            commit=True
        ):
        """
        A method which creates a table in a database.

        Args:
            command (str): SQL command.
            commit (bool, optional): Commit the current transaction. Defaults to True.

        Raises:
            SyntaxError: A simple and quick check if CREATE TABLE exists in the command.
        """
        try:
            if "CREATE TABLE" not in command.upper():
                raise SyntaxError("No CREATE TABLE command found!")

            self.conn = self.connect()
    
            cursor = self.conn.cursor()
    
            cursor.execute(command)
            print("Table has been created successfully!")
            
            cursor.close()
    
            if commit: self.conn.commit()

        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
        
        finally:
            self.close()
    

    def drop_table(self,
            command:str,
            commit=True
        ):
        """
        A method which drops a table in a database.

        Args:
            command (str): SQL command.
            commit (bool, optional): Commit the current transaction. Defaults to True.

        Raises:
            SyntaxError: A simple and quick check if DROP TABLE exists in the command.
        """
        try:
            if "DROP TABLE" not in command.upper():
                raise SyntaxError("No DROP TABLE command found!")
            
            self.conn = self.connect()

            cursor = self.conn.cursor()

            cursor.execute(command)
            print("Table has been deleted successfully!")

            cursor.close()

            if commit: self.conn.commit()

        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
        
        finally:
            self.close()
    
    
    def insert_into_table(self, 
            command: str, 
            values: tuple,
            has_dict=False, 
            multiple=False, 
            commit=True
        ):
        """
        A method which inserts new data in a table in a database.

        Args:
            command (str): SQL command.
            values (tuple): The values for each variable in the command.
            has_dict (bool, optional): True, if values contain dictionary. Defaults to False.
            multiple (bool, optional): True, if execution of many rows. Defaults to False.
            commit (bool, optional): Commit the current transaction. Defaults to True.

        Raises:
            SyntaxError: A simple and quick check if INSERT INTO exists in the command.
        """
        try:
            if "INSERT INTO" not in command.upper():
                raise SyntaxError("No INSERT INTO command found!")

            self.conn = self.connect()
            
            if has_dict:
                cursor = self.conn.cursor(cursor_factory=DictCursor)
            else: cursor = self.conn.cursor()
            
            if not multiple:
                cursor.execute(command, values)
                print(f"Insertion of object is done!")
            else:
                cursor.executemany(command, values)
                for _ in values:
                    print(f"Insertion of object is done!")
            
            cursor.close()
    
            if commit: self.conn.commit()

        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
        
        finally:
            self.close()
    
    
    def row_count(self, 
            name: str, 
            commit=True
        ) -> int:
        """
        A method which counts the rows of a table in a database.
        
        Args:
            name (str): Table's name.
            commit (bool, optional): Commit the current transaction. Defaults to True.

        Returns:
            int: The number of rows.
        """
        try:
            self.conn = self.connect()
    
            cursor = self.conn.cursor()
            
            command = f"SELECT COUNT(*) from {name};"
            cursor.execute(command)
            
            count = cursor.fetchone()[0]
            
            cursor.close()
    
            if commit: self.conn.commit()
            
            return count

        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
        
        finally:
            self.close()
    

    def update_table(self,
            command: str, 
            values: tuple, 
            commit= True
        ):
        """
        A method which updates a table in a database. 

        Args:
            command (str): SQL command.
            values (tuple): Values for each variable in the command.
            commit (bool, optional): Commit the current transaction. Defaults to True.

        Raises:
            SyntaxError: A simple and quick check if UPDATE exists in the command.
        """
        try:
            if "UPDATE" not in command.upper():
                raise SyntaxError("No UPDATE command found!")

            self.conn = self.connect()

            cursor = self.conn.cursor()

            cursor.execute(command, values)
            print(f"Update of values {values} is done!")
            
            cursor.close()

            if commit: self.conn.commit()

        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
        
        finally:
            self.close()
    

    def query_data(self, 
            command: str, 
            fetch="fetchall", 
        ):
        """
        A method which queries data from a table in a database.

        Args:
            command (str): SQL command.
            fetch (str, optional): Retrieves rows. Defaults to "fetchall".

        Raises:
            SyntaxError: A simple and quick check if SELECT exists in the command.

        Returns:
            The retrieved rows.
        """
        try:
            if "SELECT" not in command.upper():
                raise SyntaxError("No SELECT command found!")

            self.conn = self.connect()

            cursor = self.conn.cursor()

            cursor.execute(command)

            if fetch == 'fetchall': data = cursor.fetchall()

            cursor.close()

            return data
        
        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
        
        finally:
            self.close()
    

    def delete_data(self, 
            command: str, 
            values: tuple, 
            commit=True
        ):
        """
        A method which deletes data from a table in a database.

        Args:
            command (str): SQL command.
            values (tuple): Values for each variable in the command.
            commit (bool, optional): Commit the current transaction. Defaults to True.

        Raises:
            SyntaxError: A simple and quick check if DELETE exists in the command.
        """
        try:
            if "DELETE" not in command.upper():
                raise SyntaxError("No DELETE command found!")
   
            self.conn = self.connect()

            cursor = self.conn.cursor()

            cursor.execute(command, values)

            del_rows = cursor.rowcount

            print(f"Deletion of {del_rows} rows with values {values} is done!")

            cursor.close()

            if commit: self.conn.commit()

        except (Exception, psycopg2.DatabaseError) as e:
            print(e)
        
        finally:
            self.close()
