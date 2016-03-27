from .common import *
import logging

logger = logging.getLogger(__name__)

try:
    from .local import *  # noqa
except ImportError as error:
    logger.warn('No local.py settings file found')
