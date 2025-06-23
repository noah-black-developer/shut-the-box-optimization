# largestFirst.py
# Desc: Move strategy that select the largest #'s available whenever possible.
# Author: Noah Black (noah.black0425@gmail.com)
# Last Updated: June 22st, 2025


# NATIVE IMPORTS.
# THIRD-PARTY IMPORTS.
# LOCAL IMPORTS.
from .base import PlayerInterface
from game.core import GameInstance


# CLASSES.
class LargestFirstPlayer(PlayerInterface):
    def select(self, game: GameInstance) -> list[int]:
        # If a single tile move is available, use that.
        if len(game.validMoves[0]) == 1:
            return game.validMoves[0]

        # Otherwise, search over the available options and find the move with the largest # contained.
        largestNumFound = -1
        move = []
        for possibleMove in game.validMoves:
            largestNumInMove = possibleMove[-1]
            if largestNumInMove > largestNumFound:
                largestNumFound = largestNumInMove
                move = possibleMove

        # Return the selected move.
        return move
    
class LargePreserveLowPlayer(PlayerInterface):
    def select(self, game: GameInstance) -> list[int]:
        # If a single tile move is available, use that.
        if len(game.validMoves[0]) == 1:
            return game.validMoves[0]
        
        # Otherwise, attempt to search for the move that preserves the lowest digits.
        highestMinDigit = -1
        move = []
        for possibleMove in game.validMoves:
            if highestMinDigit < possibleMove[0]:
                highestMinDigit = possibleMove[0]
                move = possibleMove

        # Return the selected move.
        return move


# MAIN ENTRY.
def main() -> None:
    raise NotImplementedError

if __name__=="__main__":
    main()
