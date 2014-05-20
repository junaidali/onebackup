__author__ = 'junaid'

import sys
import os.path
import logging

# Program variables
HOME_DIR = os.path.expanduser('~')
DEFAULT_DB_FILE_NAME = 'onebackup.db'

# Logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def main():
    logger.info("Launching OneBackup")
    return 0

def config():
    """
    Configures the one backup tool. Performs the following
    1. Initializes the configuration database
    2. Locates paths to important tools and updates within the database
    """
    logger.info("Configuring OneBackup")
    logger.debug("Checking for default configuration database at %s" %os.path.join(HOME_DIR, DEFAULT_DB_FILE_NAME))
    if os.path.isfile(os.path.join(HOME_DIR, DEFAULT_DB_FILE_NAME)):
        logger.debug("Default database configuration database found")
    else:
        logger.warn("Default database configuration database not found. Asking user for custom database location")
        db = raw_input('Please provide configuration database location:\t')
        if os.path.isfile(db):
            logger.debug("Configuration file %s already exists" %db)
        else:
            logger.warn("Configuration file %s not found. Will create new file" %db)

    return 0

if __name__ == '__main__':
    sys.exit(main())