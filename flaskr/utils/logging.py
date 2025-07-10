import logging
from logging.config import dictConfig
import os

# make sure the `logs/` directory exists in the correct location
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOG_DIR = os.path.join(BASE_DIR, 'logs')
os.makedirs(LOG_DIR, exist_ok=True)


app_log_file_path = os.path.join(LOG_DIR, 'app.log')
print(f"Logging to: {app_log_file_path}")
# sqlalchemy_log_file_path = os.path.join(LOG_DIR, 'sqlalchemy.log')
# wsgi_log_file_path = os.path.join(LOG_DIR, 'wsgi.log')

def setup_logging():
    dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format' : '[%(asctime)s] - %(levelname)s - %(message)s',
                'style': '%',
                'datefmt': '%Y-%m-%d %H:%M',
            }
        },
        'handlers': {
            # use this same template below for other handlers
            'app_file': {
                'class': 'logging.FileHandler',
                'filename': app_log_file_path,
                'formatter': 'default',
                'level': 'DEBUG',
                'mode': 'a',
                'encoding': 'utf-8'
            }
            # TODO: Activate once sqlalchemy connection established
            # 'sqlalchemy_file': {
            #     'class': 'logging.FileHandler',
            #     'filename': 'logs/sqlalchemy.log',
            #     'formatter': 'default',
            #     'level': 'DEBUG',
            #     'filemode': 'a',
            #     'encoding': 'UTF-8',
            # },
            # TODO: Activate once wsgi established
            # 'wsgi_file': {
            #     'class': 'logging.FileHandler',
            #     'filename': 'logs/wsgi.log',
            #     'formatter': 'default',
            #     'level': 'DEBUG',
            #     'filemode': 'a',
            #     'encoding': 'UTF-8',
            # }
        },
        'loggers': {
            # TODO: Activate once sqlalchemy connection established
            # 'sqlalchemy-engine': {
            #     'handlers': ['sqlalchemy_file'],
            #     'level': 'DEBUG',
            #     'propagate': False,
            # },
            # TODO: Activate once wsgi established
            # 'werkzeug': {
            #     'handlers': ['wsgi_file'],
            #     'level': 'ERROR',
            #     'propagate': False,
            # },
            # Add more custom loggers here
        },
        'root': {
            'level': 'DEBUG',
            'handlers': ['app_file']
        }
    })

setup_logging()
# initiate the logger
logger = logging.getLogger("app")

# callable functions to simplify logging for project
def info(msg):
    logger.info(msg)

def debug(msg):
    logger.debug(msg)

def warning(msg):
    logger.warning(msg)

def error(msg):
    logger.error(msg)

def critical(msg):
    logger.critical(msg)