from sc2.ids.unit_typeid import UnitTypeId as Units


async def build_zergling(self):
    if self.units(Units.SPAWNINGPOOL).ready.exists:
        if self.can_afford(Units.ZERGLING):
            if self.units(Units.LARVA).exists:
                await self.do(self.units(Units.LARVA).random.train(Units.ZERGLING))
                return True
    return False
