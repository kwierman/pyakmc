import dataclass


@dataclass
class Simulation:
    name: str = "sim"


@dataclass
class Run:
    number: int = 0
    simulation: Simulation


@dataclass
class Step:
    number: int = 0
    run: Run
