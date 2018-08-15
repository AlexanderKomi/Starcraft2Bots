from sc2.ids.unit_typeid import UnitTypeId as Units


async def move_drones_to_gas(self):
    if self.units(Units.EXTRACTOR).ready.exists:
        extractor = self.units(Units.EXTRACTOR).first
        for drone in self.workers.random_group_of(3):
            await self.do(drone.gather(extractor))


async def move_drones_from_gas(self):
    self.moved_workers_from_gas = True
    for drone in self.workers:
        m = self.state.mineral_field.closer_than(10, drone.position)
        await self.do(drone.gather(m.random, queue=True))
