import logging

from pyakmc.ontology import Run

from .action import Action


class RunAction(Action):
    logger = logging.getLogger("pyakmc.core.actions.run")

    def at_run_start(self, run: Run) -> None:
        return None

    def at_run_end(self, run: Run) -> None:
        return None
