import sc2
from sc2 import Race, Difficulty
from sc2.player import \
	(Bot, Computer,
	# ,Human
     )

from Zerg.zergling_rush.zergling_rush import ZergRushBot
from sc2lib.downloadedmaps import *


def execute( bot: sc2.BotAI, race: Race, realtime = False, ):
	player_config = [
		# Human(Race.Zerg),
		Bot( race, bot ),
		Computer( Race.Terran, Difficulty.Medium )
	]
    sc2.run_game( sc2.maps.get(random_map()),
                  player_config,
                  realtime=realtime
                  # , save_replay_as="ZergRushBot_ZvT.SC2Replay"
                  )


if __name__ == "__main__":
	execute(
		bot=ZergRushBot(),
		race=Race.Zerg,
		realtime=False
	)
