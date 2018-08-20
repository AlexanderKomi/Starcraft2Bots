from sc2.ids.unit_typeid import UnitTypeId as Units


async def build_queen(self):
    hatchery = self.units(Units.HATCHERY).ready.first
    if self.can_afford(Units.QUEEN):
        r = await self.do(hatchery.train(Units.QUEEN))
        if not r:
            return True
    return False
