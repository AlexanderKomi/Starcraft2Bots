from sc2.ids.ability_id import AbilityId as Abilities
from sc2.ids.unit_typeid import UnitTypeId as Units


async def research_metabolicboost(self):
    if self.vespene >= 100:
        sp = self.units(Units.SPAWNINGPOOL).ready
        if sp.exists and self.minerals >= 100:
            await self.do(sp.first(Abilities.RESEARCH_ZERGLINGMETABOLICBOOST))
            return True
    return False
