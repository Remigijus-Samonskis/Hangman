import logging


def hangman_logging():
    logging.basicConfig(
        filename="logs/hangman.logs",
        format="%(asctime)s - %(levelname)s - %(module)s - %(message)s - %(process)s - %(pathname)s",
        filemode="w",
        level=logging.DEBUG,
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    return logging.getLogger(__name__)
