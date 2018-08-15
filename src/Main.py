import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer


from Zerg.zergling_rush import ZergRushBot
from sc2lib.downloadedmaps import *

realtime = True


def main():
    sc2.run_game(sc2.maps.get(DownloadedMaps().AcidPlant), [
        Bot(Race.Zerg, ZergRushBot()),
        Computer(Race.Terran, Difficulty.Easy)
    ], realtime=realtime
                 # , save_replay_as="ZergRushBot_ZvT.SC2Replay"
                 )


if __name__ == "__main__":
    main()
