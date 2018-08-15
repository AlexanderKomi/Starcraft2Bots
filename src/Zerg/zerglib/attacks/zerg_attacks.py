from sc2.ids.unit_typeid import UnitTypeId as Units

import Zerg.zerglib.common_lib as common_lib


async def all_in(self):
    if not self.units(Units.HATCHERY).ready.exists:
        for unit in self.workers | self.units(Units.ZERGLING) | self.units(Units.QUEEN):
            await self.do(unit.attack(self.enemy_start_locations[0]))
        return


async def attack_with_zerglings(self):
    target = common_lib.find_target(self)
    for zl in self.units(Units.ZERGLING).idle:
        await self.do(zl.attack(target))
