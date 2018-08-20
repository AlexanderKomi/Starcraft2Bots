from sc2.ids.unit_typeid import UnitTypeId as Units


async def build_drone(self):
    if self.can_afford(Units.DRONE):
        if self.units(Units.LARVA).exists:
            await self.do(self.units(Units.LARVA).random.train(Units.DRONE))
            return True
    return False
