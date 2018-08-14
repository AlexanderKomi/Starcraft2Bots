from sc2.constants import *
from sc2.ids.ability_id import AbilityId as Abilities
from sc2.ids.unit_typeid import UnitTypeId as Units

import Zerg.zerglib.common_lib as common_lib


async def attack_with_zerglings(self):
    target = common_lib.find_target(self, self.iteration)
    for zl in self.units(Units.ZERGLING).idle:
        await self.do(zl.attack(target))


async def inject(self):
    hatchery = self.units(Units.HATCHERY).ready.first
    for queen in self.units(Units.QUEEN).idle:
        abilities = await self.get_available_abilities(queen)
        if AbilityId.EFFECT_INJECTLARVA in abilities:
            await self.do(queen(Abilities.EFFECT_INJECTLARVA, hatchery))


async def research_metabolicboost(self):
    if self.vespene >= 100:
        sp = self.units(Units.SPAWNINGPOOL).ready
        if sp.exists and self.minerals >= 100 and not self.mboost_started:
            await self.do(sp.first(Abilities.RESEARCH_ZERGLINGMETABOLICBOOST))
            self.mboost_started = True

        if not self.moved_workers_from_gas:
            self.moved_workers_from_gas = True
            for drone in self.workers:
                m = self.state.mineral_field.closer_than(10, drone.position)
                await self.do(drone.gather(m.random, queue=True))


async def build_overlord(self):
    if (self.supply_used == self.supply_cap - 2):
        if self.can_afford(Units.OVERLORD) and self.units(Units.LARVA).exists:
            await self.do(self.units(Units.LARVA).random.train(Units.OVERLORD))


async def build_zergling(self):
    if self.units(Units.SPAWNINGPOOL).ready.exists:
        if self.units(Units.LARVA).exists and self.can_afford(Units.ZERGLING):
            await self.do(self.units(Units.LARVA).random.train(Units.ZERGLING))


async def build_drone(self):
    if self.drone_counter < 3:
        if self.can_afford(Units.DRONE):
            self.drone_counter += 1
            await self.do(self.units(Units.LARVA).random.train(Units.DRONE))


async def build_hatch(self):
    if self.minerals > 300:
        if self.can_afford(Units.HATCHERY):
            await self.expand_now()


async def build_eco_hatch(self):
    if self.minerals > 500:
        if self.can_afford(Units.HATCHERY):
            hatchery = self.units(Units.HATCHERY).ready.first
            for d in range(4, 15):
                pos = hatchery.position.to2.towards(self.game_info.map_center, d)
                if await self.can_place(Units.HATCHERY, pos):
                    self.spawning_pool_started = True
                    await self.do(self.workers.random.build(Units.HATCHERY, pos))
                    break


async def move_drones_to_gas(self):
    if self.units(Units.EXTRACTOR).ready.exists and not self.moved_workers_to_gas:
        self.moved_workers_to_gas = True
        extractor = self.units(Units.EXTRACTOR).first
        for drone in self.workers.random_group_of(3):
            await self.do(drone.gather(extractor))


async def build_extractors(self):
    if self.can_afford(Units.EXTRACTOR):
        drone = self.workers.random
        target = self.state.vespene_geyser.closest_to(drone.position)
        err = await self.do(drone.build(Units.EXTRACTOR, target))
        if not err:
            self.extractor_started = True


async def build_spawningpool(self):
    hatchery = self.units(Units.HATCHERY).ready.first
    if self.can_afford(Units.SPAWNINGPOOL):
        for d in range(4, 15):
            pos = hatchery.position.to2.towards(self.game_info.map_center, d)
            if await self.can_place(Units.SPAWNINGPOOL, pos):
                drone = self.workers.closest_to(pos)
                err = await self.do(drone.build(Units.SPAWNINGPOOL, pos))
                if not err:
                    self.spawning_pool_started = True
                    break


async def build_queen(self):
    hatchery = self.units(Units.HATCHERY).ready.first
    if self.can_afford(Units.QUEEN):
        r = await self.do(hatchery.train(Units.QUEEN))
        if not r:
            self.queeen_started = True


async def all_in(self):
    if not self.units(Units.HATCHERY).ready.exists:
        for unit in self.workers | self.units(Units.ZERGLING) | self.units(Units.QUEEN):
            await self.do(unit.attack(self.enemy_start_locations[0]))
        return
