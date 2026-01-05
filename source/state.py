# Tracks game state, and completed status of each game

import machine
from machine import Pin

import led


class GameState:
    def __init__(self):
        self.completed_games = {
            "DTMF": False,
            "HiLo": False,
            "Kode": False,
            "Simon": False,
            "RPS": False
        }

    def complete(self, game_name):
        if game_name in self.completed_games:
            self.completed_games[game_name] = True
            print(f"Game {game_name} marked as completed.")
        else:
            print(f"Game {game_name} not found in game state.")

    def is_completed(self, game_name):
        return self.completed_games.get(game_name, False)

    def reset(self, game_name):
        if game_name in self.completed_games:
            self.completed_games[game_name] = False
            print(f"Game {game_name} has been reset to not completed.")
        else:
            print(f"Game {game_name} not found in game state.")


gamestate = GameState()
