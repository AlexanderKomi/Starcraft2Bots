import sc2
from sc2 import Race

import Main
import Zerg.zerglib.zerg_lib as zerg_lib
import Zerg.zergling_rush.attack as zerg_rush_attack
import Zerg.zergling_rush.buildings as zerg_rush_buildings
import Zerg.zergling_rush.research as zerg_rush_research
import Zerg.zergling_rush.units as zerg_rush_units
import sc2lib.common_lib as common_lib
from Zerg.zerglib.counter import Counter


class ZergRushBot(sc2.BotAI):
    counter: Counter = Counter()

    async def on_step(self, iteration):
        await common_lib.glhf(self, iteration)
        await self.starter_build()

    async def starter_build(self):
        await zerg_rush_attack.attack(self)
        await zerg_rush_units.build_units(self)
        await zerg_rush_buildings.buildings(self)
        await zerg_rush_research.research_metabolicboost( self )
        await zerg_lib.inject(self)

    def __repr__(self):
        return '+++ Zerg Rush : Time to rush! :) +++'


if __name__ == "__main__":
    Main.execute( ZergRushBot(), Race.Zerg, realtime=False )
