from sc2.ids.ability_id import AbilityId as Abilities
from sc2.ids.unit_typeid import UnitTypeId as Units


async def research( bot ):
	await research_metabolicboost( bot )
	await research_gilclaws( bot )


async def research_metabolicboost(self):
    if self.vespene >= 100:
        sp = self.units(Units.SPAWNINGPOOL).ready
        if sp.exists and self.minerals >= 100:
            await self.do(sp.first(Abilities.RESEARCH_ZERGLINGMETABOLICBOOST))
            return True
    return False


async def research_gilclaws( self ):
	if self.units( Units.LAIR ).exists and not self.already_pending( Units.LAIR ):
		if self.vespene >= 100:
			rw = self.units( Units.ROACHWARREN ).ready
			if rw.exists and self.minerals >= 100:
				await self.do( rw.first( Abilities.RESEARCH_GLIALREGENERATION ) )
				return True
	return False
