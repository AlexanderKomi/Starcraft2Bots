import random


def find_target(self):
    # return self.known_enemy_structures.random_or(self.enemy_start_locations[0]).position
    return self.known_enemy_units.random_or(self.enemy_start_locations[0]).position


def select_target(self):
    if self.known_enemy_units.exists:
        return random.choice(self.known_enemy_units).position


async def glhf(self, iteration=0):
    if iteration == 0:
        await self.chat_send("(glhf)")
