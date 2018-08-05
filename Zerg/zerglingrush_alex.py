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

    async def glhf(self, iteration):
        if iteration == 0:
            await self.chat_send("(glhf)")

    async def attack_with_zerglings(self):
        target = self.known_enemy_structures.random_or(self.enemy_start_locations[0]).position
        for zl in self.units(ZERGLING).idle:
            await self.do(zl.attack(target))

    async def inject(self):
        hatchery = self.units(HATCHERY).ready.first
        for queen in self.units(QUEEN).idle:
            abilities = await self.get_available_abilities(queen)
            if AbilityId.EFFECT_INJECTLARVA in abilities:
                await self.do(queen(EFFECT_INJECTLARVA, hatchery))

    async def research_metabolicboost(self):
        if self.vespene >= 100:
            sp = self.units(SPAWNINGPOOL).ready
            if sp.exists and self.minerals >= 100 and not self.mboost_started:
                await self.do(sp.first(RESEARCH_ZERGLINGMETABOLICBOOST))
                self.mboost_started = True

            if not self.moved_workers_from_gas:
                self.moved_workers_from_gas = True
                for drone in self.workers:
                    m = self.state.mineral_field.closer_than(10, drone.position)
                    await self.do(drone.gather(m.random, queue=True))

    async def build_overlord(self):
        if (self.supply_used == self.supply_cap-2):
            if self.can_afford(OVERLORD) and self.units(LARVA).exists:
                await self.do(self.units(LARVA).random.train(OVERLORD))

    async def build_zergling(self):
        if self.units(SPAWNINGPOOL).ready.exists:
            if self.units(LARVA).exists and self.can_afford(ZERGLING):
                await self.do(self.units(LARVA).random.train(ZERGLING))

    async def build_drone(self):
        if self.drone_counter < 3:
            if self.can_afford(DRONE):
                self.drone_counter += 1
                await self.do(self.units(LARVA).random.train(DRONE))

    async def build_hatch(self):
        if self.minerals > 300:
            self.expand_now()
            #hatchery = self.units(HATCHERY).ready.first
            # for d in range(4, 15):
            #     pos = hatchery.position.to2.towards(self.game_info.map_center, d)
            #     if await self.can_place(HATCHERY, pos):
            #         self.spawning_pool_started = True
            #         await self.do(self.workers.random.build(HATCHERY, pos))
            #         break

    async def move_drones_to_gas(self):
        if self.units(EXTRACTOR).ready.exists and not self.moved_workers_to_gas:
            self.moved_workers_to_gas = True
            extractor = self.units(EXTRACTOR).first
            for drone in self.workers.random_group_of(3):
                await self.do(drone.gather(extractor))

    async def all_in(self):
        if not self.units(HATCHERY).ready.exists:
            for unit in self.workers | self.units(ZERGLING) | self.units(QUEEN):
                await self.do(unit.attack(self.enemy_start_locations[0]))
            return

    async def build_queens(self):
        hatchery = self.units(HATCHERY).ready.first

        if not self.extractor_started:
            if self.can_afford(EXTRACTOR):
                drone = self.workers.random
                target = self.state.vespene_geyser.closest_to(drone.position)
                err = await self.do(drone.build(EXTRACTOR, target))
                if not err:
                    self.extractor_started = True

        elif not self.spawning_pool_started:
            if self.can_afford(SPAWNINGPOOL):
                for d in range(4, 15):
                    pos = hatchery.position.to2.towards(self.game_info.map_center, d)
                    if await self.can_place(SPAWNINGPOOL, pos):
                        drone = self.workers.closest_to(pos)
                        err = await self.do(drone.build(SPAWNINGPOOL, pos))
                        if not err:
                            self.spawning_pool_started = True
                            break

        elif not self.queeen_started and self.units(SPAWNINGPOOL).ready.exists:
            if self.can_afford(QUEEN):
                r = await self.do(hatchery.train(QUEEN))
                if not r:
                    self.queeen_started = True


    async def on_step(self, iteration):
        await self.glhf(iteration)
        await self.attack_with_zerglings()
        await self.inject()
        await self.research_metabolicboost()
        await self.build_overlord()
        await self.build_zergling()
        await self.build_drone()
        await self.move_drones_to_gas()
        await self.build_hatch()
        await self.all_in()
        await self.build_queens()
        

def main():
    sc2.run_game(sc2.maps.get("(2)CatalystLE"), [
        Bot(Race.Zerg, ZergRushBot()),
        Computer(Race.Terran, Difficulty.Medium)
    ], realtime=True
    #, save_replay_as="ZvT.SC2Replay"
    )

if __name__ == '__main__':
    main()