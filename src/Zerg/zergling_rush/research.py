import Zerg.zerglib.zerg_lib as zerg_lib

from Zerg.zerglib.units.zerg_micro import move_drones_from_gas
from Zerg.zerglib.units.zerg_micro import move_drones_to_gas


async def research_metabolicboost( bot ):
	if not bot.counter.mboost_started:
		bot.counter.mboost_started = await zerg_lib.research_metabolicboost( bot )
		if not bot.counter.moved_workers_to_gas:  # No need for more gas :)
			bot.counter.moved_workers_to_gas = await move_drones_to_gas( bot )

	elif not bot.counter.moved_workers_from_gas:
		bot.counter.moved_workers_from_gas = await move_drones_from_gas( bot )
