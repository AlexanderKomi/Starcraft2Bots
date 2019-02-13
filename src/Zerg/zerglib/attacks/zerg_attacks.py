from sc2.ids.unit_typeid import UnitTypeId as Units

import sc2lib.common_lib as common_lib


async def all_in(self):
    if not self.units(Units.HATCHERY).ready.exists:
        for unit in self.workers | self.units(Units.ZERGLING) | self.units(Units.QUEEN):
            await self.do(unit.attack(self.enemy_start_locations[0]))
        return


async def _attack( self, unit ):
    target = common_lib.find_target(self)
    for zl in self.units( unit ).idle:
        await self.do(zl.attack(target))


async def attack_with_zerglings( self ):
	return await _attack( self, Units.ZERGLING )


async def attack_with_roaches( self ):
	return await _attack( self, Units.ROACH )
