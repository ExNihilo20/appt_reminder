import csv
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import schedule
import time
import configparser
from utils.app_logger import debug
from utils.connection import Connection 

def main():
    conn = Connection()
    conn.test_db_connection()

main()