import logging

from pyakmc.ontology import Simulation

from .action import Action


class SimulationAction(Action):
    logger = logging.getLogger("pyakmc.core.actions.run")

    def at_simulation_start(self, simulation: Simulation) -> None:
        return None

    def at_simulation_end(self, simulation: Simulation) -> None:
        return None
