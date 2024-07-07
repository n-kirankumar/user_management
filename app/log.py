"""
log.py
-------
Sets up logging for the project.
"""

import logging
from constants import LOG_SWITCH, LOG_MESSAGES

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create handlers
file_handler = logging.FileHandler('app.log')
console_handler = logging.StreamHandler()

# Set level of handlers
file_handler.setLevel(logging.DEBUG)
console_handler.setLevel(logging.DEBUG)

# Create formatters and add it to handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def log_message(level, message, **kwargs):
    """
    Logs a message with the given log level if logging is enabled.

    Args:
        level (str): The level of the log (e.g., 'debug', 'info', 'warning', 'error', 'critical').
        message (str): The message to log.
        **kwargs: Additional arguments to format the message.
    """
    if LOG_SWITCH:
        if level == 'debug':
            logger.debug(message.format(**kwargs))
        elif level == 'info':
            logger.info(message.format(**kwargs))
        elif level == 'warning':
            logger.warning(message.format(**kwargs))
        elif level == 'error':
            logger.error(message.format(**kwargs))
        elif level == 'critical':
            logger.critical(message.format(**kwargs))
