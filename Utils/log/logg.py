import logging
from datetime import datetime


# הגדרת הלוגר הגלובלי
def setup_logger():
    logger = logging.getLogger('app_logger')  # נותנים שם ללוגר כדי שיהיה קל יותר למצוא אותו
    logger.setLevel(logging.DEBUG)  # מגדירים את רמת הלוג
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


# יצירת לוגר גלובלי כך שנשתמש בו בכל הפונקציות
logger = setup_logger()


def printer(message, log_type="DEBUG"):
    if log_type == "DEBUG" or log_type.strip() == "":
        logger.debug(message)
    elif log_type == "INFO":
        logger.info(message)
    elif log_type == "WARNING":
        logger.warning(message)
    elif log_type == "ERROR":
        logger.error(message)
    elif log_type == "CRITICAL":
        logger.critical(message)
    else:
        logger.info("Unknown log type: %s", log_type)
