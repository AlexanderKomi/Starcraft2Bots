from sc2.ids.unit_typeid import UnitTypeId as Units

from Zerg.zerglib.buildings import zerg_buildings as buildings
from Zerg.zerglib.units import zerg_units as units
from Zerg.zerglib.abilities import zerg_abilities as abilities
from Zerg.zerglib.research import zerg_research as research
from Zerg.zerglib.attacks import zerg_attacks as attacks
from Zerg.zerglib.units import zerg_micro as micro


# ATTACKS
async def all_in(self):
    await attacks.all_in(self)


async def attack_with_zerglings(self):
    await attacks.attack_with_zerglings(self)


async def move_drones_to_gas(self):
    await micro.move_drones_to_gas(self)


# ABILITIES
async def inject(self):
    await abilities.inject(self)


# RESEARCH
async def research_metabolicboost(self):
    await research.research_metabolicboost(self)


# BUILD UNITS
async def build_overlord(self):
    await units.build_overlord(self)


async def build_zergling(self):
    await units.build_zergling(self)


async def build_drone(self):
    if self.drone_counter < 3:
        await units.build_drone(self)
        self.drone_counter += 1


async def build_queen(self):
    await units.build_queen(self)


# BUILDINGS
async def build_hatch(self):
    await buildings.build_hatch(self)


async def build_eco_hatch(self):
    await buildings.build_eco_hatch(self)


async def build_extractors(self):
    await buildings.build_extractors(self)


async def build_spawningpool(self):
    await buildings.build_spawningpool(self)
