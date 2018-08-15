from sc2.ids.ability_id import AbilityId as Abilities
from sc2.ids.unit_typeid import UnitTypeId as Units

from Zerg.zerglib.units.zerg_micro import move_drones_from_gas
from Zerg.zerglib.units.zerg_micro import move_drones_to_gas


async def research_metabolicboost(self):
    if self.vespene >= 100:
        if not self.mboost_started:
            sp = self.units(Units.SPAWNINGPOOL).ready
            if sp.exists and self.minerals >= 100:
                await self.do(sp.first(Abilities.RESEARCH_ZERGLINGMETABOLICBOOST))
                self.mboost_started = True

        if not self.moved_workers_from_gas:
            await move_drones_from_gas(self)
    else:
        await move_drones_to_gas(self)
