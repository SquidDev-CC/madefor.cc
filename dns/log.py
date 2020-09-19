"""Helper methods to configure the system logger."""

import asyncio
import logging
import logging.config
from typing import Any, Dict
import warnings

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

COLOURS = {
    'WARNING': YELLOW,
    'INFO': WHITE,
    'DEBUG': BLUE,
    'CRITICAL': YELLOW,
    'ERROR': RED
}

def loop_exception_handler(loop: asyncio.AbstractEventLoop, context: Dict[str, Any]) -> None:
    """A custom error handler for the loop, which stops the loop before continuing to
       the default handler

    """
    logging.error("Terminating loop due to error")
    if loop.is_running():
        loop.stop()
    loop.default_exception_handler(context)

class ColourFormatter(logging.Formatter):
    """Formats log messages using ANSI escape codes."""
    def __init__(self, *args, **kwargs): # type: ignore
        super().__init__(*args, **kwargs)

    def format(self, record: logging.LogRecord) -> str:
        msg = super().format(record)
        if record.levelname in COLOURS:
            msg = "\033[1;3%dm%s\033[0m" % (COLOURS[record.levelname], msg)
        return msg

FORMAT = "[%(asctime)s] [%(levelname)s/%(name)s] %(message)s"

def configure() -> None:
    """Configure the root logger. This should be called once when the program is
       initialised.

    """
    # Be more aggressive in capturing warnings
    logging.captureWarnings(True)
    warnings.simplefilter('default')

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Register a custom formatter, which prints things coloured with the time, level and coponent
    # name.
    col_formatter = ColourFormatter(FORMAT, None, '%')
    col_formatter.default_msec_format = "%s.%03d"

    str_handler = logging.StreamHandler()
    str_handler.setFormatter(col_formatter)
    str_handler.setLevel(logging.INFO)

    logger.addHandler(str_handler)
