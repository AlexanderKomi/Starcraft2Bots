import sc2

import Zerg.zerglib.zerg_lib as zerg_lib
import Zerg.zergling_rush.attack as zerg_rush_attack
import Zerg.zergling_rush.buildings as zerg_rush_buildings
import Zerg.zergling_rush.units as zerg_rush_units
import sc2lib.common_lib as common_lib
from Zerg.zerglib.counter import Counter
from Zerg.zerglib.units.zerg_micro import move_drones_from_gas
from Zerg.zerglib.units.zerg_micro import move_drones_to_gas


class ZergRushBot(sc2.BotAI):
    counter: Counter = Counter()

    async def on_step(self, iteration):
        await common_lib.glhf(self, iteration)
        await self.starter_build()

    async def starter_build(self):
        await zerg_rush_attack.attack(self)
        await zerg_rush_units.build_units(self)
        await zerg_rush_buildings.buildings(self)
        await self.research_metabolicboost()
        await zerg_lib.inject(self)

    async def research_metabolicboost(self):
        if not self.counter.mboost_started:
            self.counter.mboost_started = await zerg_lib.research_metabolicboost(self)
            if not self.counter.moved_workers_to_gas:  # No need for more gas :)
                self.counter.moved_workers_to_gas = await move_drones_to_gas(self)

        elif not self.counter.moved_workers_from_gas:
            self.counter.moved_workers_from_gas = await move_drones_from_gas(self)

    def __repr__(self):
        return '+++ Zerg Rush : Time to rush! :) +++'
