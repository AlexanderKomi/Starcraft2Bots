import sc2
from sc2.ids.unit_typeid import UnitTypeId as Units

import Zerg.zerglib.common_lib as common_lib
import Zerg.zerglib.zerg_lib as zerg_lib
from Zerg.zerglib.units.zerg_micro import move_drones_from_gas
from Zerg.zerglib.units.zerg_micro import move_drones_to_gas


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
        await common_lib.glhf(self, iteration)
        await self.starter_build()

    async def starter_build(self):
        await self.attack()
        await self.build_units()
        await self.buildings()
        await self.research_metabolicboost()
        await zerg_lib.inject(self)

    async def attack(self):
        if self.units(Units.ZERGLING).amount > 10:
            await zerg_lib.attack_with_zerglings(self)
            await zerg_lib.all_in(self)

    async def build_units(self):
        await self.drone_overlord_management()

        if self.mboost_started:
            await zerg_lib.build_zergling(self)
            if not self.queeen_started:
                self.queeen_started = await zerg_lib.build_queen(self)

    async def drone_overlord_management(self):
        # Fancy 14 - Pool Drone management :D
        if self.supply_left <= 4:  # Not too many Overlords
            if not self.already_pending(Units.OVERLORD):
                await zerg_lib.build_overlord(self)

        if self.drone_counter < 3:
            if self.supply_cap == 14:
                if self.already_pending(Units.OVERLORD):
                    if await zerg_lib.build_drone(self):
                        self.drone_counter += 1
            else:
                if await zerg_lib.build_drone(self):
                    self.drone_counter += 1

    async def buildings(self):
        if not self.extractor_started:
            if self.drone_counter > 1:
                self.extractor_started = await zerg_lib.build_extractors(self)
        elif not self.spawning_pool_started:
            self.spawning_pool_started = await zerg_lib.build_spawningpool(self)

        elif self.mboost_started and not self.units(Units.LARVA).exists:
            await zerg_lib.build_hatch(self)

    async def research_metabolicboost(self):
        if not self.mboost_started:
            self.mboost_started = await zerg_lib.research_metabolicboost(self)
            if not self.moved_workers_to_gas:  # No need for more gas :)
                self.moved_workers_to_gas = await move_drones_to_gas(self)

        elif not self.moved_workers_from_gas:
            self.moved_workers_from_gas = await move_drones_from_gas(self)

    def __repr__(self):
        return '+++ Zerg Rush : Time to rush! :) +++'
