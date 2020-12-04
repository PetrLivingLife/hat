from os import getcwd, path
import logging
import logging.config
import logging.handlers

from yaml import safe_load
from box import Box

from utilities import check_or_create_dir


def load_yaml(filepath):
    with open(filepath, 'r') as f:
        return safe_load(f.read())


def setup_logging(log_config_filepath=None,
                  logs_output_path=None,
                  logging_level=None):
    logs_location = logs_output_path or path.join(getcwd(),
                                                  "logs",)
    check_or_create_dir(logs_location)

    log_config_filepath = log_config_filepath or path.join(getcwd(),
                                                           "configuration",
                                                           "logging_configuration.yaml", )

    if path.exists(log_config_filepath):
        logging.config.dictConfig(load_yaml(log_config_filepath))
        if logging_level:
            root_logger = logging.getLogger()
            root_logger.handlers[0].setLevel(logging_level)
            root_logger.handlers[1].setLevel(logging_level)

    else:
        logging_level = logging_level or logging.INFO
        standard_formatter = logging.Formatter('{asctime} [{levelname:<8}]: {message}', style='{')
        debug_formatter = logging.Formatter('{asctime} [{levelname:<8}] {name}.{funcName}(): {message}', style='{')

        # Console setup
        ch = logging.StreamHandler()
        ch.setLevel(logging_level)
        ch.setFormatter(standard_formatter)

        # Standard log file
        fh = logging.handlers.RotatingFileHandler(path.join(logs_location, "uat.log"),
                                                  maxBytes=1048576,
                                                  backupCount=10,)
        fh.setLevel(logging_level)
        fh.setFormatter(standard_formatter)

        # Debug
        fh_debug = logging.handlers.RotatingFileHandler(path.join(logs_location, "uat_debug.log"),
                                                        maxBytes=1048576,
                                                        backupCount=10)
        fh_debug.setLevel(logging.DEBUG)
        fh_debug.setFormatter(debug_formatter)

        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)
        root_logger.addHandler(ch)
        root_logger.addHandler(fh)
        root_logger.addHandler(fh_debug)

        logger = logging.getLogger(__name__)

        logger.error(f"Couldn't load logging configuration from '{log_config_filepath}'. "
                     "Used default configuration. "
                     f"Logs: {logs_location} "
                     f"Level: {logging_level} "
                     )


def load_config(profile):
    filepath = path.join(getcwd(),
                         "configuration",
                         f"{profile}.yaml")
    return Box(load_yaml(filepath))
