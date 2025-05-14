from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configparser import ConfigParser
from app.proj_utils.app_logger import info
import os
# grab mysql strings
parser = ConfigParser()
# outside package scope
config_path = os.path.expanduser("~/Documents/projects/proj_configs/conf/appt_reminder.config")
parser.read(config_path, encoding="UTF-8")

print(f'has section mysql: {parser.has_section('mysql')}')
info("grabbed configs")


# connection params
mysql_user = parser.get('mysql', 'mysql_user')
mysql_pass = parser.get('mysql', 'mysql_pass')
mysql_host = parser.get('mysql', 'mysql_host')
mysql_port = parser.get('mysql', 'mysql_port')
mysql_dbname = parser.get('mysql', 'mysql_dbname')

info("assigned connection params")
connection_string = f'mysql+pymysql://{mysql_user}:{mysql_pass}@{mysql_host}:{mysql_port}/{mysql_dbname}'
info('loaded connection string')

# pass string into engine
mysql_engine = create_engine(connection_string, echo=True)
info('passed conn_str into engine')
# create a high-level session to be used throughout application
Session = sessionmaker(bind=mysql_engine, autoflush=False, autocommit=False)
info("engine and sessionmaker initialized")