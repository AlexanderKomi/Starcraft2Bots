import sc2
from sc2 import Race, Difficulty
from sc2.player import \
    Bot \
    , Computer \
    # ,Human

from Zerg.zergling_rush import ZergRushBot
from sc2lib.downloadedmaps import *

real_time = False
player_config = [
    # Human(Race.Zerg),
        Bot(Race.Zerg, ZergRushBot()),
    Computer(Race.Terran, Difficulty.Medium)
]


def main():
    sc2.run_game(sc2.maps.get(random_map()),
                 player_config,
                 realtime=real_time
                 # , save_replay_as="ZergRushBot_ZvT.SC2Replay"
                 )


if __name__ == "__main__":
    main()
