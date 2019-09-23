"""
Common utilities for resplendent.
"""

import logging

from logdecorator import log_exception

exclog = log_exception(  # pylint: disable=invalid-name
    logging.ERROR, "Error handling function.", on_exceptions=(Exception,), reraise=True
)
