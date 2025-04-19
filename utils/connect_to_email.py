import csv
import smtplib
from email.mime.text import MIMEText
from configparser import ConfigParser

# Proton Bridge SMTP settings (running locally)
parser = ConfigParser()
configs = parser.read("../conf/email_creds.conf", encoding="UTF-8")
pb_configs = configs['proton_bridge']

PB_HOSTNAME = pb_configs['pb_hostname']
PB_IMAP_PORT = pb_configs['pb_IMAP_port']
PB_SMTP_PORT = pb_configs['pb_SMTP_port']
PB_USERNAME = pb_configs['pb_username']
PB_PASSWORD = pb_configs['pb_password']
PB_SECURITY = pb_configs['pb_security']

# TODO: fill in the rest of the script