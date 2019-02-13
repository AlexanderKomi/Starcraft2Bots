from sc2.ids.unit_typeid import UnitTypeId as Units


async def build_extractors(self):
    if self.can_afford(Units.EXTRACTOR):
        drone = self.workers.random
        target = self.state.vespene_geyser.closest_to(drone.position)
        err = await self.do(drone.build(Units.EXTRACTOR, target))
        if not err:
            return True
    return False


async def build_spawningpool(self):
    if self.can_afford(Units.SPAWNINGPOOL):
        hatchery = self.units(Units.HATCHERY).ready.first
        for d in range(4, 15):
            pos = hatchery.position.to2.towards(self.game_info.map_center, d)
            if await self.can_place(Units.SPAWNINGPOOL, pos):
                drone = self.workers.closest_to(pos)
                err = await self.do(drone.build(Units.SPAWNINGPOOL, pos))
                if not err:
                    return True
    return False


async def build_roachwarren(self):
	if self.units( Units.SPAWNINGPOOL ).exists and not self.already_pending( Units.SPAWNINGPOOL ):
		if not (self.units( Units.ROACHWARREN ).exists or self.already_pending( Units.ROACHWARREN )):
			if self.can_afford( Units.ROACHWARREN ):
				hatchery = self.units( Units.HATCHERY ).ready.first
				for d in range( 6, 35 ):
					pos = hatchery.position.to2.towards( self.game_info.map_center, d )
					if await self.can_place( Units.ROACHWARREN, pos ):
						drone = self.workers.closest_to( pos )
						err = await self.do( drone.build( Units.ROACHWARREN, pos ) )
						if not err:
							return True
	return False


async def build_hatch(self):
    if self.can_afford(Units.HATCHERY):
        await self.expand_now()
        return True
    return False


async def build_eco_hatch(self):
    if self.can_afford(Units.HATCHERY):
        hatchery = self.units(Units.HATCHERY).ready.first
        for d in range(4, 15):
            pos = hatchery.position.to2.towards(self.game_info.map_center, d)
            if await self.can_place(Units.HATCHERY, pos):
                self.spawning_pool_started = True
                await self.do(self.workers.random.build(Units.HATCHERY, pos))
                return True
    return False
