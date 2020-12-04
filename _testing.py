import logging

from os import path, getcwd

from configuration import configuration


configuration.setup_logging(
    # log_config_filepath="h",
    # logs_output_path=path.join(getcwd(), "logs"),
    # logging_level=logging.DEBUG,
)

logger = logging.getLogger(__name__)

logger.debug("logger debug msg here")
logger.info("logger info msg here")
logger.warning("logger warning msg here")
logger.error("logger error msg here")
logger.critical("logger critical msg here")
