import os
import logging

def get_logger_verbosity():
    if 'AUD_VERBOSE' in os.environ:
        return logging.DEBUG

    root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    git = os.path.join(root, '.git')
    if os.path.exists(git):
        return logging.DEBUG

    return logging.WARNING