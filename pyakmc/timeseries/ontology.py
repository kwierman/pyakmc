from pyakmc.core.ontology import Run, Simulation, Step


class TimeSeriesSimulation(Simulation):
    run_start_time_epoch_ns: float = 0.0


class TimeSeriesRun(Run):
    run_time_epoch_ns: float = 0.0


class TimeSeriesStep(Step):
    step_time_epoch_ns: float = 0.0
