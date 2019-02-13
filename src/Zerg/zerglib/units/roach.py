from sc2.ids.unit_typeid import UnitTypeId as Units


async def build_roach( bot ):
	if bot.units( Units.ROACHWARREN ).exists and not bot.already_pending( Units.ROACHWARREN ):
		if bot.units( Units.LARVA ).exists:
			if bot.can_afford( Units.ROACH ):
				await bot.do( bot.units( Units.LARVA ).random.train( Units.ROACH ) )
                return True
    return False
