# { "Depends": "py-genlayer:test" }
from genlayer import *
import json


class PlayerRegistry(gl.Contract):
    """
    Chain Quest: Player Registry
    On-chain player profile system.
    Stores player names, levels, and XP.
    No external API needed - pure on-chain logic.
    """
    player_names: TreeMap[str, str]
    player_levels: TreeMap[str, u256]

    def __init__(self):
        self.player_names = TreeMap()
        self.player_levels = TreeMap()

    @gl.public.write
    def register_player(self, address: str, name: str) -> str:
        self.player_names[address] = name
        self.player_levels[address] = u256(1)
        return "Player " + name + " registered at Level 1"

    @gl.public.write
    def level_up(self, address: str) -> str:
        current = self.player_levels.get(address, u256(0))
        self.player_levels[address] = current + u256(1)
        name = self.player_names.get(address, "Unknown")
        new_level = current + u256(1)
        return name + " leveled up to " + str(new_level)

    @gl.public.view
    def get_player(self, address: str) -> str:
        name = self.player_names.get(address, "Not Found")
        level = self.player_levels.get(address, u256(0))
        return "Name: " + name + " | Level: " + str(level)
