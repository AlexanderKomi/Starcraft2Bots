import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.constants import *

class SentdeBot(sc2.BotAI):
    async def on_step(self,iteration):
        await self.distribute_workers()
        await self.build_workers()

    async def build_workers(self):
        if self.can_afford(DRONE):
            await self.do(self.units(LARVA).random.train(DRONE))

run_game(
    maps.get("AbyssalReefLE"),
    [ 
        Bot(Race.Zerg, SentdeBot()),
        Computer(Race.Terran, Difficulty.Easy)
    ], 
    realtime=True)
