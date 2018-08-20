from Zerg.zerglib.units import drone
from Zerg.zerglib.units import overlord
from Zerg.zerglib.units import queen
from Zerg.zerglib.units import zergling


async def build_zergling(self):
    return zergling.build_zergling(self)


async def build_overlord(self):
    return overlord.build_overlord(self)


async def build_efficiently_overlords(self):
    return overlord.build_efficiently_overlords(self)


async def build_drone(self):
    return drone.build_drone(self)


async def build_queen(self):
    return queen.build_queen(self)
