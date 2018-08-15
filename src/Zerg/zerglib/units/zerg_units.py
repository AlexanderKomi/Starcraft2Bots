from sc2.ids.unit_typeid import UnitTypeId as Units


async def build_zergling(self):
    if self.units(Units.SPAWNINGPOOL).ready.exists:
        if self.units(Units.LARVA).exists and self.can_afford(Units.ZERGLING):
            await self.do(self.units(Units.LARVA).random.train(Units.ZERGLING))


async def build_overlord(self):
    if self.supply_used >= self.supply_cap - 2:
        if self.can_afford(Units.OVERLORD) and self.units(Units.LARVA).exists:
            await self.do(self.units(Units.LARVA).random.train(Units.OVERLORD))


async def build_drone(self):
    if self.can_afford(Units.DRONE):
        await self.do(self.units(Units.LARVA).random.train(Units.DRONE))


async def build_queen(self):
    hatchery = self.units(Units.HATCHERY).ready.first
    if self.can_afford(Units.QUEEN):
        r = await self.do(hatchery.train(Units.QUEEN))
        if not r:
            self.queeen_started = True
