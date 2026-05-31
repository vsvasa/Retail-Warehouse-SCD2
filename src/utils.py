import logging
import os
import configparser
import mysql.connector 


def setup_logger():
    log_path = "logs/warehouse.log"
    os.makedirs("logs",exist_ok = True)

    logging.basicConfig(
        filename = log_path,
        level = logging.INFO,
        format = "%(asctime)s - %(levelname)s - %(message)s",
       
    )
    return logging

def read_config():
    config = configparser.ConfigParser()
    config.read("config/config.ini")

    return config

def create_connection():
    try:
        config = read_config()
        return mysql.connector.connect(
            host = config.get("mysql","host"),
            user = config.get("mysql","user"),
            password = config.get("mysql","password"),
            database = config.get("mysql","database")
        )
    except Exception as e:
        logger.error(f"Error connecting to database: {e}")
        return None