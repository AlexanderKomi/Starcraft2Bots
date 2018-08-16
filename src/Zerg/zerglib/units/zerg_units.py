from sc2.ids.unit_typeid import UnitTypeId as Units


async def build_zergling(self):
    if self.units(Units.SPAWNINGPOOL).ready.exists:
        if self.can_afford(Units.ZERGLING):
            if self.units(Units.LARVA).exists:
                await self.do(self.units(Units.LARVA).random.train(Units.ZERGLING))
                return True
    return False


async def build_overlord(self):
    if self.can_afford(Units.OVERLORD):
        if self.units(Units.LARVA).exists:
            await self.do(self.units(Units.LARVA).random.train(Units.OVERLORD))
            return True
    return False


async def build_drone(self):
    if self.can_afford(Units.DRONE):
        if self.units(Units.LARVA).exists:
            await self.do(self.units(Units.LARVA).random.train(Units.DRONE))
            return True
    return False


async def build_queen(self):
    hatchery = self.units(Units.HATCHERY).ready.first
    if self.can_afford(Units.QUEEN):
        r = await self.do(hatchery.train(Units.QUEEN))
        if not r:
            return True
    return False
