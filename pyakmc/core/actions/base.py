import logging

from pyakmc.configuration import Configuration


class BaseAction:
    logger = logging.getLogger("pyakmc.core.actions.base")
    config: Configuration

    def configure(self, configuration: Configuration) -> None:
        self.config = configuration
