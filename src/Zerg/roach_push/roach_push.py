import sc2
from sc2 import Race

import Main
import sc2lib.common_lib as common_lib
from Zerg.roach_push.attack import *
from Zerg.roach_push.buildings import *
from Zerg.roach_push.research import *
from Zerg.roach_push.units import *
from Zerg.zerglib.counter import Counter


class RoachPushBot( sc2.BotAI ):
	counter: Counter = Counter()

	async def on_step( self, iteration ):
		await common_lib.glhf( self, iteration )
		await self.starter_build()

	async def starter_build( self ):
		await attack( self )
		await build_units( self )
		await buildings( self )
		await research( self )
		await zerg_lib.inject( self )

	def __repr__( self ):
		return '+++ Roach Push : Time to rush! :) +++'


if __name__ == "__main__":
	Main.execute( RoachPushBot(), Race.Zerg, realtime=False )
