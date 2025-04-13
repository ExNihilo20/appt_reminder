import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    style="%",
    datefmt="%Y-%m-%d %H:%M",
    filemode="a",
    encoding="UTF-8",
    filename="logs/appt_remind.log"
)

def debug(message:str):
    logging.debug(message)

def info(message:str):
    logging.info(message)

def warning(message:str):
    logging.warning(message)

def error(message:str):
    logging.error(message, exc_info=True)

def critical(message:str):
    logging.critical(message, exc_info=True)

