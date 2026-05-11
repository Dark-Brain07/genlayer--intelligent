# { "Depends": "py-genlayer:test" }
from genlayer import *


class PlayerRegistry(gl.Contract):
    """
    Chain Quest: Player Registry
    On-chain player profile system.
    Stores player names and levels.
    """
    player_names: TreeMap[str, str]
    player_levels: TreeMap[str, str]

    def __init__(self):
        self.player_names = TreeMap()
        self.player_levels = TreeMap()

    @gl.public.write
    def register_player(self, player_id: str, name: str) -> str:
        self.player_names[player_id] = name
        self.player_levels[player_id] = "1"
        return "Player " + name + " registered at Level 1"

    @gl.public.write
    def level_up(self, player_id: str) -> str:
        current_str = self.player_levels[player_id]
        current = int(current_str)
        new_level = current + 1
        self.player_levels[player_id] = str(new_level)
        name = self.player_names[player_id]
        return name + " leveled up to " + str(new_level)

    @gl.public.view
    def get_player(self, player_id: str) -> str:
        name = self.player_names[player_id]
        level = self.player_levels[player_id]
        return "Name: " + name + " | Level: " + level
