from Zerg.zerglib.units import drone
from Zerg.zerglib.units import overlord
from Zerg.zerglib.units import queen
from Zerg.zerglib.units import roach
from Zerg.zerglib.units import zergling


async def build_zergling(self):
    return await zergling.build_zergling(self)


async def build_overlord(self):
    return await overlord.build_overlord(self)


async def build_efficiently_overlords(self):
    return await overlord.build_efficiently_overlords(self)


async def build_drone(self):
    return await drone.build_drone(self)


async def build_queen(self):
    return await queen.build_queen(self)


async def build_roach(self):
    return await roach.build_roach(self)
