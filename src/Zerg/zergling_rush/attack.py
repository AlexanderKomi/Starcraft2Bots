from sc2.ids.unit_typeid import UnitTypeId as Units

import Zerg.zerglib.zerg_lib as zerg_lib


async def attack(bot):
    if bot.units(Units.ZERGLING).amount > 10:
        await zerg_lib.attack_with_zerglings(bot)
        await zerg_lib.all_in(bot)
