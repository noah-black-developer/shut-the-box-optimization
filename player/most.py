# most.py
# Desc: Move strategies that always selects as many numbers as possible.
# Author: Noah Black (noah.black0425@gmail.com)
# Last Updated: June 22st, 2025


# NATIVE IMPORTS.
# THIRD-PARTY IMPORTS.
# LOCAL IMPORTS.
from .base import PlayerInterface
from game.core import GameInstance


# CLASSES.
class MostThenSmall(PlayerInterface):
    def select(self, game: GameInstance) -> list[int]:
        # Find the length of the longest available move list, then isolate.
        mostTilesPossible = len(game.validMoves[-1])
        largeMoves = [ move for move in game.validMoves if len(move) == mostTilesPossible ]

        # Return the first element from the list, which generally has the lowest #'s possible.
        return largeMoves[0]

class MostThenLarge(PlayerInterface):
    def select(self, game: GameInstance) -> list[int]:
        # Find the length of the longest available move list, then isolate.
        mostTilesPossible = len(game.validMoves[-1])
        largeMoves = [ move for move in game.validMoves if len(move) == mostTilesPossible ]

        # Return the last element from the list, which generally has the largest #'s possible.
        return largeMoves[-1]

# MAIN ENTRY.
def main() -> None:
    raise NotImplementedError

if __name__=="__main__":
    main()
