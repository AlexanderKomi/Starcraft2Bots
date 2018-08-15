import sc2
from sc2.ids.unit_typeid import UnitTypeId as Units

import Zerg.zerglib.common_lib as common_lib
import Zerg.zerglib.zerg_lib as zerg_lib


class ZergRushBot(sc2.BotAI):

    def __init__(self):
        self.drone_counter = 0
        self.extractor_started = False
        self.spawning_pool_started = False
        self.moved_workers_to_gas = False
        self.moved_workers_from_gas = False
        self.queeen_started = False
        self.mboost_started = False
        self.iteration = 0

    async def on_step(self, iteration):
        self.iteration = iteration
        await common_lib.glhf(self, iteration)
        await self.starter_build()

    async def starter_build(self):
        if not self.extractor_started:
            if self.drone_counter > 1:
                await zerg_lib.build_extractors(self)
        elif not self.spawning_pool_started:
            self.spawning_pool_started = await zerg_lib.build_spawningpool(self)
        elif not self.queeen_started and self.units(Units.SPAWNINGPOOL).ready.exists and self.mboost_started:
            await zerg_lib.build_queen(self)
        await self.attack()
        await self.build_units()
        await self.buildings()
        await self.research()
        await zerg_lib.inject(self)
        await zerg_lib.all_in(self)

    async def attack(self):
        await zerg_lib.attack_with_zerglings(self)

    async def build_units(self):
        if self.mboost_started:
            await zerg_lib.build_zergling(self)

        if self.supply_used >= (self.supply_cap - 4):
            if not self.already_pending(Units.OVERLORD):
                await zerg_lib.build_overlord(self)

        if self.drone_counter < 3:
            if self.can_afford(Units.DRONE):
                if self.supply_cap == 14:
                    if self.already_pending(Units.OVERLORD):
                        await zerg_lib.build_drone(self)
                        self.drone_counter += 1
                else:
                    await zerg_lib.build_drone(self)
                    self.drone_counter += 1

    async def buildings(self):
        if self.mboost_started and not self.units(Units.LARVA).exists:
            await zerg_lib.build_hatch(self)

    async def research(self):
        await zerg_lib.research_metabolicboost(self)

    def __repr__(self):
        return 'Zerg Rush : Time to rush! :)'
