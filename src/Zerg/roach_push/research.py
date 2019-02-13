import Zerg.zerglib.zerg_lib as zerg_lib

from Zerg.zerglib.units.zerg_micro import move_drones_to_gas


async def research( bot ):
	await research_metabolicboost( bot )
	await research_gil( bot )


async def research_gil( bot ):
	if not bot.counter.gilclaws_started:
		bot.counter.gilclaws_started = await zerg_lib.research_gil( bot )


async def research_metabolicboost( bot ):
	if not bot.counter.mboost_started:
		bot.counter.mboost_started = await zerg_lib.research_metabolicboost( bot )
		if not bot.counter.moved_workers_to_gas:
			bot.counter.moved_workers_to_gas = await move_drones_to_gas( bot )
