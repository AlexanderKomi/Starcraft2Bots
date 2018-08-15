def find_target(self):
    return self.known_enemy_structures.random_or(self.enemy_start_locations[0]).position


async def glhf(self, iteration=0):
    if iteration == 0:
        await self.chat_send("(glhf)")
