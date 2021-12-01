#!/usr/bin/python
from database import DataBase
from tables import Tables

from base.base_handler import AbstractBaseHandler
from model.resnet50_fpn import DetectBodyKeypoints
from model.utils.render import Render
from utils.blob import BlobData


class Configuration:
    config: str = '/app/dbms/db_config.ini'
    starting_section: str = 'starting_point'
    ending_section: str = 'ending_point'

    CREATE_DATABASE: str = 'create_database'
    CREATE_TABLE: str = 'create_table'
    INSERT_TABLE: str = 'insert_table'
    ROW_COUNT: str = 'row_count'



class CreateDatabaseHandler(Configuration, AbstractBaseHandler):
    
    def __init__(self, command: str):
        self.dbms = DataBase(CreateDatabaseHandler.config, CreateDatabaseHandler.starting_section)
        self.command = command
        

    def handle(self, req: str) -> str:
        if req == CreateDatabaseHandler.CREATE_DATABASE:
            self.dbms.create_database(self.command)

        else:
            return super().handle(req)


class CreateTableHandler(Configuration, AbstractBaseHandler):

    def __init__(self, command: str):
        self.dbms = Tables(CreateTableHandler.config, CreateTableHandler.ending_section)
        self.command = command
    

    def handle(self, req: str) -> str:
        if req == CreateTableHandler.CREATE_TABLE:
            self.dbms.create_table(self.command)  

        else:
            return super().handle(req)


class InsertTableHandler(Configuration, AbstractBaseHandler):

    def __init__(self, command: str, values: tuple):
        self.dbms = Tables(InsertTableHandler.config, InsertTableHandler.ending_section)
        self.command = command
        self.values = values
    

    def handle(self, req: str) -> str:
        if req == InsertTableHandler.INSERT_TABLE:
            self.dbms.insert_into_table(self.command, self.values)

        else:
            return super().handle(req)
    

    def insert_img_into_table(self, command: str, values: tuple):
        self.dbms.insert_into_table(command, values, has_dict=True) 


class RowCountTableHandler(Configuration, AbstractBaseHandler):

    def __init__(self, name: str):
        self.dbms = Tables(RowCountTableHandler.config, RowCountTableHandler.ending_section)
        self.name = name
    

    def handle(self, req: str) -> str:
        if req == RowCountTableHandler.ROW_COUNT:
            return self.dbms.row_count(self.name)   

        else:
            return super().handle(req)



class ImageHandler(BlobData):

    def __init__(self):
        self.dt = DetectBodyKeypoints()
    

    def get_3d_keypoints(self, path_to_img: str):
        detections_keypoints = self.dt.get_body_keypoints(path_to_img)
        json_joints_coords, dict_joints_coords = self.dt._json(detections_keypoints)

        return json_joints_coords, dict_joints_coords
    

    @staticmethod
    def rendered_image(
        path_to_img: str,
        jsn: str, 
        save_img_path: str
    ):
        Render.render(path_to_img, jsn, save_img_path)


    @staticmethod
    def to_bytea(path_to_img: str):
        return ImageHandler.image_to_bytesarray(path_to_img)