import logging

def setup_logger(name="MedcialAssistantLogger", level=logging.INFO):
    """Sets up and returns a logger with the specified name and level."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # Create formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    # Add the handler to the logger
    if not logger.hasHandlers():
        logger.addHandler(ch)

    return logger


logger=setup_logger()

logger.info("RAG prcoess started")
logger.debug("Bebugging")
logger.error("Failed to load")
logger.critical("Critical message")