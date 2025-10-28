# db_config.py
import os

# PostgreSQL connection details from Render environment variables
host = os.environ.get("DB_HOST")      # e.g., dpg-d4098lv5r7bs73a9js1g-a.oregon-postgres.render.com
user = os.environ.get("DB_USER")      # e.g., scp_directory_user
password = os.environ.get("DB_PASS")  # e.g., Btmg0lFsk5stbUZ295GM0fEOUCVVC3Jm
database = os.environ.get("DB_NAME")  # e.g., scp_directory
port = os.environ.get("DB_PORT", 5432)
