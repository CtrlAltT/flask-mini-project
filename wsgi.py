# Import flask instance
from app import app
import logging

# Instantiate logger
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    logger.info('Starting service...')
    app.run(host="0.0.0.0", port=8080)
