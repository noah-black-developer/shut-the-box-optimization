# train.py
# Desc: Player class that supports both training off of a variety of game data and applying training in runs.
#   Uses a monte-carlo style optimization strategy, selecting random moves for game states, then using results to inform future moves.
# Author: Noah Black (noah.black0425@gmail.com)
# Last Updated: June 21st, 2025


# NATIVE IMPORTS.
# THIRD-PARTY IMPORTS.
# LOCAL IMPORTS.
from game.core import GameInstance
from .base import PlayerInterface


# CONSTANTS.
DEFAULT_ITERATIONS: int = 100000


# CLASSES.
class TrainedInterface(PlayerInterface):
    def select(self, game: GameInstance) -> list[int]:
        ...

    def train(self, outputFile: str = "training.csv") -> None:
        ...

    def trainState(self, state: dict[str, list[int]], tiles: list[int], roll: int, iterations: int = DEFAULT_ITERATIONS) -> dict[]
        ...

# MAIN ENTRY.
def main() -> None:
    raise NotImplementedError

if __name__=="__main__":
    main()
