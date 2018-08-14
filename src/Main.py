import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer

from Zerg.zergling_rush import ZergRushBot


def main():
    sc2.run_game(sc2.maps.get("(2)CatalystLE"), [
        Bot(Race.Zerg, ZergRushBot()),
        Computer(Race.Terran, Difficulty.Medium)
    ], realtime=False
                 # , save_replay_as="ZvT.SC2Replay"
    )