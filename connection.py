from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PySide6.QtWidgets import QApplication, QTableView
from PySide6.QtCore import Qt
import os
import sys

#TODO : заменить плейсхолдеры на $число
class Data:
    def __init__(self, db_type='QPSQL', host='localhost', db_name='monkeos_database', 
                 user='dmitry', password='admin') -> None:
        super(Data, self).__init__()
        self.db_name = db_name

        self.db = QSqlDatabase.addDatabase(db_type)
        self.db.setHostName(host)
        self.db.setDatabaseName(str(self.db_name))
        self.db.setUserName(user)
        self.db.setPassword(password)
            
        if not self.db.open():
            raise Exception(f"Cannot open database: {self.db.lastError().text()}")
        
    def execute_query(self, query_text, params=None):
        query = QSqlQuery(self.db)
        query.prepare(query_text)

        if params:
            if isinstance(params, dict):
                for key, value in params.items():
                    query.bindValue(key, value)
            else:
                for i, value in enumerate(params):
                    query.bindValue(f":{i+1}", value)
        
        if not query.exec():
            raise Exception(f"Query error: {query.lastError().text()}")

    def exec_query_list(self, query_text, params=None):
        query = QSqlQuery(self.db)
        query.prepare(query_text)
        if params:
            for i, param in enumerate(params, start=0):
                query.bindValue(i, param)

        if not query.exec():
            raise Exception(f"Query error: {query.lastError().text()}")

    def add_cam_list(self,
                   connection_string, fps, 
                   resolution, description=None):
        self.exec_query_list('''INSERT INTO cameras (connection_string, description, fps, resolution) VALUES ($1, $2, $3, $4);
        ''', [
            connection_string,
            description,
            fps,
            resolution
        ])

    def add_cam_exec(self,
                   connection_string, fps, 
                   resolution, description=None):
        query = QSqlQuery(self.db)
        if not query.exec(f'INSERT INTO cameras (connection_string, description, fps, resolution) VALUES (\'{connection_string}\', \'{description}\', {fps}, \'{resolution}\')'):
            raise Exception(f"Query error: {query.lastError().text()}")

    def create_tables(self):
        query = QSqlQuery(self.db)
        if not query.exec('''
        CREATE TABLE IF NOT EXISTS cameras (
            id SERIAL PRIMARY KEY,
            connection_string TEXT NOT NULL,
            description TEXT,
            fps INTEGER,
            resolution TEXT
        );
        '''):
            print(f"Failed to create cameras table: {query.lastError().text()}")

        if not query.exec('''
        CREATE TABLE IF NOT EXISTS zones (
            id SERIAL PRIMARY KEY,
            camera_id INTEGER REFERENCES cameras(id) ON DELETE CASCADE,
            coordinates TEXT NOT NULL,
            description TEXT
        );
        '''):
            print(f"Failed to create zones table: {query.lastError().text()}")

    def add_camera(self, 
                   connection_string, fps, 
                   resolution, description=None):
        self.execute_query('''
        INSERT INTO cameras (connection_string, description, fps, resolution)
        VALUES (:connection_string, :description, :fps, :resolution);
        ''', {
            ':connection_string': connection_string,
            ':description': description,
            ':fps': fps,
            ':resolution': resolution
        })

    def add_zone(self, camera_id: int, coordinates: str, description: str=None):
        self.execute_query('''
        INSERT INTO zones (camera_id, coordinates, description)
        VALUES (:camera_id, :coordinates, :description);
        ''', {
            ':camera_id': camera_id,
            ':coordinates': coordinates,
            ':description': description
        })

    def update_camera(self, camera_id, 
                      new_connection_string, new_fps, 
                      new_resolution, new_description=None):
        self.execute_query('''
        UPDATE cameras
        SET connection_string = COALESCE(:connection_string, connection_string),
            description = COALESCE(:description, description),
            fps = COALESCE(:fps, fps),
            resolution = COALESCE(:resolution, resolution)
        WHERE id = :camera_id;
        ''', {
            ':connection_string': new_connection_string,
            ':description': new_description,
            ':fps': new_fps,
            ':resolution': new_resolution,
            ':camera_id': camera_id
        })

    def update_zone(self, zone_id, new_camera_id=None, new_coordinates=None, new_description=None):
        self.execute_query('''
        UPDATE zones
        SET camera_id = COALESCE(:camera_id, camera_id),
            coordinates = COALESCE(:coordinates, coordinates),
            description = COALESCE(:description, description)
        WHERE id = :zone_id;
        ''', {
            ':camera_id': new_camera_id,
            ':coordinates': new_coordinates,
            ':description': new_description,
            ':zone_id': zone_id
        })

    def delete_camera(self, camera_id):
        self.execute_query('''
        DELETE FROM cameras
        WHERE id = :camera_id;
        ''', {
            ':camera_id': camera_id
        })

    def delete_zone(self, zone_id):
        self.execute_query('''
        DELETE FROM zones
        WHERE id = :zone_id;
        ''', {
            ':zone_id': zone_id
        })
