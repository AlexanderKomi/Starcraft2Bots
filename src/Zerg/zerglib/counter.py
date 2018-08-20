class Counter:
    drone_counter: int
    zergling_counter: int

    extractor_started: bool
    spawning_pool_started: bool
    moved_workers_to_gas: bool
    moved_workers_from_gas: bool
    queen_started: bool
    mboost_started: bool

    def __init__(self):
        self.drone_counter = 0
        self.zergling_counter = 0

        self.extractor_started = False
        self.spawning_pool_started = False
        self.moved_workers_to_gas = False
        self.moved_workers_from_gas = False
        self.queen_started = False
        self.mboost_started = False
