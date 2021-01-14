import logging

from os import path, getcwd

from configuration import configuration


configuration.setup_logging(
    # log_config_filepath="h",
    # logs_output_path=path.join(getcwd(), "logs"),
    # logging_level=logging.DEBUG,
)

log = logging.getLogger(__name__)

log.debug("logger debug msg here")
log.info("logger info msg here")
log.warning("logger warning msg here")
log.error("logger error msg here")
log.critical("logger critical msg here")
