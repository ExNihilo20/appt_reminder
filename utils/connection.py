from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from configparser import ConfigParser
from utils.app_logger import debug, info, error
import os
from database.students import Student
from database.messages import Message


# grab mysql strings
parser = ConfigParser()
# outside package scope
config_path = os.path.expanduser("~/Documents/projects/proj_configs/conf/appt_reminder.config")
parser.read(config_path, encoding="UTF-8")
print(f'has section mysql: {parser.has_section('mysql')}')
info("grabbed configs")

class Connection:
    def __init__(self):
        # conntion params
        self.mysql_user = parser.get('mysql', 'mysql_user')
        self.mysql_pass = parser.get('mysql', 'mysql_pass')
        self.mysql_host = parser.get('mysql', 'mysql_host')
        self.mysql_port = parser.get('mysql', 'mysql_port')
        self.mysql_dbname = parser.get('mysql', 'mysql_dbname')
        info("assigned connection params")
        self.connection_string = f'mysql+pymysql://{self.mysql_user}:{self.mysql_pass}@{self.mysql_host}:{self.mysql_port}/{self.mysql_dbname}'
        info('loaded connection string')
        # pass string into engine
        self.engine = create_engine(self.connection_string)
        info('passed conn_str into engine')
        
    
    def test_db_connection(self):
        # test the connection
        with self.engine.connect() as conn:
            result = conn.execute(text("select 'hello world'"))
            print(result.all())
    
    def create_user(self):
        # TODO: create method body
        pass
    
    def create_message(self):
        # TODO: create method body
        pass