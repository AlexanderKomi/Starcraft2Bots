from Zerg.zerglib.abilities import zerg_abilities as abilities
from Zerg.zerglib.attacks import zerg_attacks as attacks
from Zerg.zerglib.buildings import zerg_buildings as buildings
from Zerg.zerglib.research import zerg_research as research
from Zerg.zerglib.units import zerg_micro as micro
from Zerg.zerglib.units import zerg_units as units


# ATTACKS
async def all_in(self):
    await attacks.all_in(self)


async def attack_with_zerglings(self):
    await attacks.attack_with_zerglings(self)


# MICRO
async def move_drones_to_gas(self):
    return await micro.move_drones_to_gas(self)


async def move_drones_from_gas(self):
    return await micro.move_drones_from_gas(self)


# ABILITIES
async def inject(self):
    await abilities.inject(self)


# RESEARCH
async def research_metabolicboost(self):
    return await research.research_metabolicboost(self)


# BUILD UNITS
async def build_overlord(self):
    await units.build_overlord(self)


async def build_efficiently_overlords(self):
    return units.build_efficiently_overlords(self)


async def build_zergling(self):
    return await units.build_zergling(self)


async def build_drone(self):
    return await units.build_drone(self)


async def build_queen(self):
    return await units.build_queen(self)


# BUILDINGS
async def build_hatch(self):
    return await buildings.build_hatch(self)


async def build_eco_hatch(self):
    return await buildings.build_eco_hatch(self)


async def build_extractors(self):
    return await buildings.build_extractors(self)


async def build_spawningpool(self):
    return await buildings.build_spawningpool(self)
