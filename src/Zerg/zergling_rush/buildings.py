from sc2.ids.unit_typeid import UnitTypeId as Units

import Zerg.zerglib.zerg_lib as zerg_lib


async def buildings(bot):
    if not bot.counter.extractor_started:
        if bot.counter.drone_counter > 1:
            bot.counter.extractor_started = await zerg_lib.build_extractors(bot)
    elif not bot.counter.spawning_pool_started:
        bot.counter.spawning_pool_started = await zerg_lib.build_spawningpool(bot)

    elif bot.counter.mboost_started and not bot.units(Units.LARVA).exists:
        await zerg_lib.build_hatch(bot)
