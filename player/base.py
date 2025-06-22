# base.py
# Desc: Base class for Shut-the-Box 'players' i.e. play strategies.
#   Defines the minimum required methods to interact with a game instance.
# Author: Noah Black (noah.black0425@gmail.com)
# Last Updated: June 21st, 2025


# NATIVE IMPORTS.
from abc import ABC, abstractmethod
# THIRD-PARTY IMPORTS.
# LOCAL IMPORTS.
from game.core import GameInstance


# CLASSES.
class PlayerInterface(ABC):
    @abstractmethod
    def select(self, game: GameInstance) -> list[int]:
        """Given a specified game state, select a single move.

        :param game: Current game state to pick a move from
        :type game: list[bool]
        :return: Selected move
        :rtype: list[int]
        """

    def roundAsStr(self, game: GameInstance) -> str:
        output = "\n"
        output += self.tilesAsStr(game)
        output += "\n\n"
        output += self.diceAsStr(game)
        return output
    
    def tilesAsStr(self, game: GameInstance) -> str:
        tilePrintoutLines = ["", "", "", "", "" ]
        for tileIndex, tileWasUsed in enumerate(game.tiles):
            if not tileWasUsed:
                tilePrintoutLines[0] += "+---+"
                tilePrintoutLines[1] += "|   |"
                tilePrintoutLines[2] += f"| {tileIndex + 1} |"
                tilePrintoutLines[3] += "|   |"
                tilePrintoutLines[4] += "+---+"
            else:
                tilePrintoutLines[0] += "     "
                tilePrintoutLines[1] += "     "
                tilePrintoutLines[2] += "     "
                tilePrintoutLines[3] += "+---+"
                tilePrintoutLines[4] += "+---+"

        return "\n".join(tilePrintoutLines)
    
    def diceAsStr(self, game: GameInstance) -> str:
        dieValue1, dieValue2 = game.lastRoll
        dieTotal = dieValue1 + dieValue2
        
        output = "+---+ +---+\n"
        output += f"| {dieValue1} | | {dieValue2} |  =  {dieTotal}\n"
        output += "+---+ +---+\n\n"

        output += "Possible moves:\n"
        if (len(game.validMoves) > 0):
            for moveIndex, move in enumerate(game.validMoves):
                moveAsStr = ", ".join(str(value) for value in move)
                output += f"  [{moveIndex}] {moveAsStr}\n"
        else:
            output += "  NONE\n"

        return output


# MAIN ENTRY.
def main() -> None:
    raise NotImplementedError

if __name__=="__main__":
    main()
