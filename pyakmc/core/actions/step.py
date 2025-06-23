import logging

from pyakmc.ontology import Step

from .action import Action


class StepAction(Action):
    logger = logging.getLogger("pyakmc.core.actions.run")

    def at_step_start(self, step: Step) -> None:
        return None

    def at_step_end(self, step: Step) -> None:
        return None
