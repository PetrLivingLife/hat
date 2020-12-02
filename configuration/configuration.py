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


def setup_logging(level=logging.INFO):
    logs_location = path.join(getcwd(),
                              # TODO remove once this is being called from main script, also in logging.cnf.yaml
                              "..",
                              "logs",)

    check_or_create_dir(logs_location)

    filepath = path.join(getcwd(),
                         # TODO once this is being run from main script
                         # "configuration",
                         "logging_configuration.yaml", )

    if path.exists(filepath):
        logging.config.dictConfig(load_yaml(filepath))

    else:
        standard_formatter = logging.Formatter('%(asctime)s - %(levelname)-8s: %(message)s')
        debug_formatter = logging.Formatter('%(asctime)s - %(levelname)-8s - %(name)10s.%(funcName)15s() : %(message)s')

        # Console setup
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(standard_formatter)

        # Standard log file
        fh = logging.handlers.RotatingFileHandler(path.join(logs_location, "uat.log"),
                                                  maxBytes=1048576,
                                                  backupCount=10,)
        fh.setLevel(level)
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

        root_logger.error(f"Couldn't load logging configuration from '{filepath}'. "
                          "Used default configuration. "
                          f"Logs: {logs_location} "
                          f"Level: {level} "
                          )


def load_config(profile):
    filepath = path.join(getcwd(),
                         # TODO once this is being run from main script
                         # "configuration",
                         f"{profile}.yaml")
    return Box(load_yaml(filepath))


# Testing
if __name__ == '__main__':
    cnf = load_config("twitter")
    setup_logging()

    logger = logging.getLogger()
    print(logger.handlers)

    # logger.debug("logger debug msg here")
    # logger.info("logger info msg here")
    # logger.warning("logger warn msg here")

    logging.debug("debug msg here")
    logging.info("info msg here")
    logging.warning("warning msg here")
