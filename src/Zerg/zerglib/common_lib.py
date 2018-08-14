def find_target(self, iteration):
    return self.known_enemy_structures.random_or(self.enemy_start_locations[0]).position


async def glhf(self, iteration):
    if iteration == 0:
        await self.chat_send("(glhf)")


if __name__ == "__main__":
    pass
