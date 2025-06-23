import logging

from pyakmc.ontology import Simulation

from .base import BaseAction


class SimulationAction(BaseAction):
    logger = logging.getLogger("pyakmc.core.actions.run")

    def at_sim_start(self, simulation: Simulation) -> None:
        return None

    def at_sim_end(self, simulation: Simulation) -> None:
        return None
