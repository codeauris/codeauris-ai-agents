import os
import sqlite3
from dotenv import load_dotenv
import logging
from datetime import datetime

# import environment variables from .env file
load_dotenv()
DB_FOLDER = os.getenv("DB_FOLDER")
db_path = os.getenv("DB_FOLDER_PATH")

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp-gateway")

def create_db_path():
    # Folder for DB - One directory above
    os.makedirs(DB_FOLDER, exist_ok=True)  # Ensure folder exists

    # Full path to the DB file
    db_path = os.path.join(DB_FOLDER, "mcp_gateway.db")
    print("DB path:", db_path)
    return db_path

def init_database():
    """Initialize SQLite database"""
    db_path = create_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create tables for various operations
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            id TEXT PRIMARY KEY,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            context TEXT,
            response TEXT,
            model TEXT,
            tokens_used INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            id TEXT PRIMARY KEY,
            title TEXT,
            content TEXT,
            tags TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS file_operations (
            id TEXT PRIMARY KEY,
            operation TEXT,
            file_path TEXT,
            status TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    print("tables created")
    conn.commit()
    conn.close()


async def store_conversation(prompt: str, context: str, response: str, model: str, tokens: int):
    """Store conversation in database"""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO conversations (id, context, response, model, tokens_used) VALUES (?, ?, ?, ?, ?)",
            (f"conv_{datetime.now().isoformat()}", f"{context}\n{prompt}", response, model, tokens)
        )
        conn.commit()
        conn.close()
    except Exception as e:
        logger.error(f"Failed to store conversation: {e}")


async def log_file_operation(operation: str, file_path: str, status: str):
    """Log file operations"""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO file_operations (id, operation, file_path, status) VALUES (?, ?, ?, ?)",
            (f"op_{datetime.now().isoformat()}", operation, file_path, status)
        )
        conn.commit()
        conn.close()
    except Exception as e:
        logger.error(f"Failed to log file operation: {e}")