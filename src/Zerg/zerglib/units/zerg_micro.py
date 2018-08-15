from sc2.ids.unit_typeid import UnitTypeId as Units


async def move_drones_to_gas(self):
    if self.units(Units.EXTRACTOR).ready.exists and not self.moved_workers_to_gas:
        self.moved_workers_to_gas = True
        extractor = self.units(Units.EXTRACTOR).first
        for drone in self.workers.random_group_of(3):
            await self.do(drone.gather(extractor))
