import pickle
import socket as Socket
from configparser import ConfigParser
from ftplib import FTP
import mysql.connector
from configs.servers_config import FTP_props, APP_props, DB_props


def get_config():
    config = ConfigParser()
    config.read('servers_props.ini')
    return config


def connect_to_db():
    conn = mysql.connector.connect(host=DB_props.HOST, user=DB_props.USER, password=DB_props.PWD, database=DB_props.DB)
    return conn


def upload_video(video, path):
    ftp = FTP('')
    ftp.connect(FTP_props.HOST, FTP_props.PORT)
    ftp.login(FTP_props.USER, FTP_props.PWD)
    ftp.storbinary('STOR ' + path + '.mp4', video)
    ftp.quit()


def send_to_app(candidate):
    socket = Socket.socket()
    socket.connect((APP_props.HOST, APP_props.PORT))
    data = pickle.dumps(candidate)
    socket.sendall(data)
    socket.close()
