from sc2.ids.unit_typeid import UnitTypeId as Units


async def build_overlord(self):
    if self.can_afford(Units.OVERLORD):
        if self.units(Units.LARVA).exists:
            await self.do(self.units(Units.LARVA).random.train(Units.OVERLORD))
            return True
    return False


async def build_efficiently_overlords(self):
    if self.supply_left <= 4:  # Not too many Overlords
        if not self.already_pending(Units.OVERLORD):
            await build_overlord(self)
