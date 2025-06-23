import logging

from pyakmc.ontology import Run

from .base import BaseAction


class RunAction(BaseAction):
    logger = logging.getLogger("pyakmc.core.actions.run")

    def at_run_start(self, run: Run) -> None:
        return None

    def at_run_end(self, run: Run) -> None:
        return None
