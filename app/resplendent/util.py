"""
Common utilities for resplendent.
"""

from logdecorator import log_exception

exclog = log_exception(  # pylint: disable=invalid-name
    "Error handling function.", on_exceptions=(Exception,), reraise=True
)
