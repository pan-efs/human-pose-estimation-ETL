#!/usr/bin/python
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
                return res
    

    @staticmethod
    def processing_client(rootdir: str, savedir: str, start_from: int):

        img_handler = ImageHandler()
        cls_insert_table = InsertTableHandler('',()) #empty
        id = start_from
        
        for img in os.listdir(rootdir):
            img_path, save_path = os.path.join(rootdir, img), os.path.join(savedir, img)
             
            original_to_bytea = img_handler.to_bytea(img_path)

            json_joints_coords, dict_joints_coords = img_handler.get_3d_keypoints(img_path)
        
            img_handler.rendered_image(img_path, json_joints_coords, save_path)

            rendered_to_bytea = img_handler.to_bytea(save_path)
            
            insert_command = f"INSERT INTO {name_of_table} (id, name, original_img, rendered_img, keypoints) values (%s, %s, %s, %s, %s);"
            insert_values = (id, img, original_to_bytea, rendered_to_bytea, Json(dict_joints_coords))
            
            try:
                cls_insert_table.insert_img_into_table(insert_command, insert_values)
                id += 1
            except: continue


###---Run client---###
CONFIG = '/app/dbms/db_config.ini'
SECTION = 'postgresql'

postgresql_details = Config(CONFIG, SECTION).config_parser()

name_of_db = postgresql_details['name_of_db']
name_of_table = postgresql_details['name_of_table']
rootdir = postgresql_details['rootdir']
savedir = postgresql_details['savedir']


database = CreateDatabaseHandler(f"CREATE DATABASE {name_of_db};")
table = CreateTableHandler(f"CREATE TABLE {name_of_table} (id INT PRIMARY KEY, name CHAR(50) UNIQUE, original_img BYTEA, rendered_img BYTEA, keypoints JSONB);")
row_count = RowCountTableHandler(f"{name_of_table}")


# Chain
database.set_next(table).set_next(row_count)

print("Create database > Create Table > Row count")
start_from = Client.create_client(database)

print(f"Start processing the {name_of_db} database and {name_of_table} table...")
Client.processing_client(rootdir, savedir, start_from + 1)