import logging

from pyakmc.core.configuration import Configuration


class Action:
    logger = logging.getLogger("pyakmc.core.actions.base")
    config: Configuration

    def configure(self, configuration: Configuration) -> None:
        self.config = configuration
