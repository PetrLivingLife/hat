"""
Contains platform drivers ready to use in tests.
"""
import logging

import drivers


log = logging.getLogger(__name__)


all = (
    drivers.Firefox,
    drivers.Chromium,
    drivers.Webkit,
    # IOS,
    # ANDROID,
    )


def get_driver_by_name(name: str):
    try:
        return {driver.name: driver for driver in all}[name]
    except KeyError:
        log.error(f"Platform driver not found or configured properly: '{name}'")
        # TODO exit properly
