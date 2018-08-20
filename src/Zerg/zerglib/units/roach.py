from sc2.ids.unit_typeid import UnitTypeId as Units


async def build_roach(self):
    if self.can_afford(Units.ROACH):
        if self.units(Units.ROACHWARREN).exists:
            if self.units(Units.LARVA).exists:
                await self.do(self.units(Units.LARVA).random.train(Units.ROACH))
                return True
    return False
