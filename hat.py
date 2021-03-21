"""Runner, controls running individual platforms and their drivers\n
Sits on top - hence the name. Plus hat=helper for application testing, haha.
"""
import logging

from configuration import RegisteredDrivers


log = logging.getLogger(__name__)


# TODO Add loading configuration and adding it here
def start_platform_driver(driver_to_start: str, *args, **kwargs):
    driver = RegisteredDrivers.get_driver_by_name(driver_to_start)
    try:
        return driver().start(*args, **kwargs)
    except TypeError as e:
        log.error(f"{e}")
        if "Can't instantiate abstract class" in str(e):
            log.error(f"Add implementation to your driver: {e}")
        raise e
