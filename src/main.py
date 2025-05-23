import bot

import logging
from rich.logging import RichHandler

from dotenv import load_dotenv
from os import getenv

if __name__ == "__main__":
    # Set up Rich logging as the only handler
    root_logger = logging.getLogger()
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
    rich_handler = RichHandler(rich_tracebacks=True)
    root_logger.addHandler(rich_handler)
    root_logger.setLevel(logging.DEBUG)
    root_logger.propagate = False

    # Remove all handlers from discord loggers and set only our handler
    for name in logging.root.manager.loggerDict:
        if name.startswith("discord"):
            logger = logging.getLogger(name)
            logger.handlers = [rich_handler]
            logger.setLevel(logging.INFO)
            logger.propagate = False

    load_dotenv()
    
    default_cogs = [
        "devtools.ping",
        "devtools.latency",
    ]
    client = bot.tfumb(default_cogs=default_cogs)
    client.run(getenv("DISCORD_TOKEN"))