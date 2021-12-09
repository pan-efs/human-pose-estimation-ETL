#!/usr/bin/env python3
import os

from psycopg2.extras import Json

from base.base_handler import BaseHandler
from utils.config import Config
from handlers import (
    CreateDatabaseHandler,
    CreateTableHandler,
    InsertTableHandler,
    RowCountTableHandler,
    ImageHandler,
    Configuration
)


class Client(Configuration):
    
    @staticmethod
    def create_client(base_handler: BaseHandler):
    
        for arg in [Client.CREATE_DATABASE, Client.CREATE_TABLE, Client.ROW_COUNT]:
            res = base_handler.handle(arg)
    
            if res != None:
                print(f"Row count: {res}")
    

    @staticmethod
    def processing_client(rootdir: str, savedir: str):
        """
        A method which processes all images from the source and saves them in a new directory.

        Args:
            rootdir (str): Source's directory.
            savedir (str): Save's directory.
        """

        img_handler = ImageHandler()
        cls_insert_table = InsertTableHandler('',()) #empty
        
        _values = []

        for img_name in os.listdir(rootdir):
            img_path, save_path = os.path.join(rootdir, img_name), os.path.join(savedir, img_name)
             
            original_to_bytea = img_handler.to_bytea(img_path)

            json_joints_coords, dict_joints_coords = img_handler.get_3d_keypoints(img_path)
        
            img_handler.rendered_image(img_path, json_joints_coords, save_path)

            rendered_to_bytea = img_handler.to_bytea(save_path)
            
            insert_values = (img_name, original_to_bytea, rendered_to_bytea, Json(dict_joints_coords))
            _values.append(insert_values)

        insert_command = f"INSERT INTO {name_of_table} (name, original_img, rendered_img, keypoints) values (%s, %s, %s, %s);"

        if len(_values) > 1:  
            cls_insert_table.insert_img_into_table(insert_command, _values, is_multiple=True)
        else:
            cls_insert_table.insert_img_into_table(insert_command, _values[0], is_multiple=False)


###---Run client---###
CONFIG = '/app/dbms/db_config.ini'
SECTION = 'postgresql'

postgresql_details = Config(CONFIG, SECTION).config_parser()

name_of_db = postgresql_details['name_of_db']
name_of_table = postgresql_details['name_of_table']
rootdir = postgresql_details['rootdir']
savedir = postgresql_details['savedir']


database = CreateDatabaseHandler(f"CREATE DATABASE {name_of_db};")
table = CreateTableHandler(f"CREATE TABLE {name_of_table} (name CHAR(50), original_img BYTEA, rendered_img BYTEA, keypoints JSONB);")
row_count = RowCountTableHandler(f"{name_of_table}")


# Chain
database.set_next(table).set_next(row_count)

print("Create database > Create Table > Row count")
Client.create_client(database)

print(f"Start processing the {name_of_db} database and {name_of_table} table...")
Client.processing_client(rootdir, savedir)