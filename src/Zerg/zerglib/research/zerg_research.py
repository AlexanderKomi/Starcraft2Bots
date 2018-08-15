from sc2.ids.ability_id import AbilityId as Abilities
from sc2.ids.unit_typeid import UnitTypeId as Units


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
