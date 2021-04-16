"""
Contains platform drivers ready to use in tests.
"""
import logging

from platform_drivers import Chromium, Firefox, Webkit


log = logging.getLogger(__name__)


all = (
    Firefox,
    Chromium,
    Webkit,
    # IOS,
    # ANDROID,
    )


def get_platform_driver_by_name(name: str):
    try:
        return {driver.name: driver for driver in all}[name]
    except KeyError:
        log.error(f"Platform driver not found or configured properly: '{name}'")
        # TODO exit properly
