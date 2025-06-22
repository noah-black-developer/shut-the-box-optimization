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



# MAIN ENTRY.
def main() -> None:
    raise NotImplementedError

if __name__=="__main__":
    main()
