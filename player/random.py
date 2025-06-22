# random.py
# Desc: Move strategy that select a random option from all available moves.
# Author: Noah Black (noah.black0425@gmail.com)
# Last Updated: June 21st, 2025


# NATIVE IMPORTS.
from random import randint

# THIRD-PARTY IMPORTS.
# LOCAL IMPORTS.
from .base import PlayerInterface
from game.core import GameInstance


# CLASSES.
class RandomPlayer(PlayerInterface):
    def select(self, game: GameInstance) -> list[int]:
        # Select a random move from the possible list, then return.
        randomMoveIndex = randint(0, len(game.validMoves) - 1)
        return game.validMoves[randomMoveIndex]


# MAIN ENTRY.
def main() -> None:
    raise NotImplementedError

if __name__=="__main__":
    main()
