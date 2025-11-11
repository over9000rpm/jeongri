import logging


def setup_logger():
    logging.basicConfig(
        filename="jeongri.log",  # Log file path
        level=logging.INFO,  # Logging level
        format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s",
    )


def log_info(message: str):
    logging.info(message)


def log_error(message: str):
    logging.error(message)
