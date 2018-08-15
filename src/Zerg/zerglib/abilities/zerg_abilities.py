from sc2.constants import *
from sc2.ids.ability_id import AbilityId as Abilities
from sc2.ids.unit_typeid import UnitTypeId as Units


async def inject(self):
    hatchery = self.units(Units.HATCHERY).ready.first
    for queen in self.units(Units.QUEEN).idle:
        abilities = await self.get_available_abilities(queen)
        if AbilityId.EFFECT_INJECTLARVA in abilities:
            await self.do(queen(Abilities.EFFECT_INJECTLARVA, hatchery))
