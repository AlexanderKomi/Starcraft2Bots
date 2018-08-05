from lib import zerg_lib
from lib import common_lib


import random

import sc2
from sc2 import Race, Difficulty
from sc2.constants import *
from sc2.player import Bot, Computer

class ZergRushBot(sc2.BotAI):

    def __init__(self):
        self.drone_counter = 0
        self.extractor_started = False
        self.spawning_pool_started = False
        self.moved_workers_to_gas = False
        self.moved_workers_from_gas = False
        self.queeen_started = False
        self.mboost_started = False

    async def on_step(self, iteration):
        self.iteration = iteration
        await common_lib.glhf(self,iteration)
        await zerg_lib.attack_with_zerglings(self)
        await zerg_lib.inject(self)
        await zerg_lib.research_metabolicboost(self)
        await zerg_lib.build_overlord(self)
        await zerg_lib.build_zergling(self)
        await zerg_lib.build_drone(self)
        await zerg_lib.move_drones_to_gas(self)
        await zerg_lib.build_hatch(self)
        await zerg_lib.all_in(self)
        await zerg_lib.build_queens(self)


def main():
    sc2.run_game(sc2.maps.get("(2)CatalystLE"), [
        Bot(Race.Zerg, ZergRushBot()),
        Computer(Race.Terran, Difficulty.Medium)
    ], realtime=False
    #, save_replay_as="ZvT.SC2Replay"
    )

if __name__ == '__main__':
    main()