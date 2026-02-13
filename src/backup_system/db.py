import mysql.connector
from backup_system.config import DB_CONFIG

# Create a return a new connection to the database
def get_connection():
    return mysql.connector.connect(**DB_CONFIG)