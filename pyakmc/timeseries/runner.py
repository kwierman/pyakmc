from .configuration import Configuration
from .ontology import Run, Simulation, Step


class SimRunner:

    def __init__(self, n_runs: int = 1):
        self.run_actions = []
        self.sim_actions = []
        self.step_actions = []
        self.n_runs = n_runs

    def configure(self, config=Configuration):
        self.n_runs = config.get("global.n_runs")

    def start(self): ...

    def start_sim(self, n_runs: int):
        for i in range(n_runs):
            ...

    def end_sim(self): ...
    def start_run(self): ...
    def end_run(self): ...

    def start_step(self): ...
    def end_step(self): ...
