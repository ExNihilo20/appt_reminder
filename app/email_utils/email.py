from configparser import ConfigParser
import os
"""
This script is supposed to handle all traffic to and from the email server."""

# Proton Bridge SMTP settings (running locally)
parser = ConfigParser()
configs = os.path.expanduser("~/Documents/projects/proj_configs/conf/appt_reminder.config")
pb_configs = configs['proton_bridge']
pm_configs = configs['protonmail']
carrier_configs = configs['carrier']

# TODO: parser broken. fix configs reference. use connection class as template

PB_HOSTNAME = pb_configs['pb_hostname']
PB_IMAP_PORT = pb_configs['pb_IMAP_port']
PB_SMTP_PORT = pb_configs['pb_SMTP_port']
PB_USERNAME = pb_configs['pb_username']
PB_PASSWORD = pb_configs['pb_password']
PB_SECURITY = pb_configs['pb_security']

# TODO: fill in the rest of the script
def get_sms_email():
    pass