from sc2.ids.unit_typeid import UnitTypeId as Units

from Zerg.zerglib import zerg_lib


async def build_units(bot):
    await drone_overlord_management(bot)
    await build_zerglings(bot)


async def build_zerglings(bot):
    if bot.counter.mboost_started:
        await zerg_lib.build_zergling(bot)
        if not bot.counter.queen_started:
            bot.counter.queen_started = await zerg_lib.build_queen(bot)


async def drone_overlord_management(bot):
    # Fancy 14 - Pool Drone management :D
    await zerg_lib.build_efficiently_overlords(bot)
    await opener(bot, 3)


async def opener(bot, drone_limit: int):
    if bot.counter.drone_counter < drone_limit:
        if bot.supply_cap == 14:
            if bot.already_pending(Units.OVERLORD):
                if await zerg_lib.build_drone(bot):
                    bot.counter.drone_counter += 1
        else:
            if await zerg_lib.build_drone(bot):
                bot.counter.drone_counter += 1
