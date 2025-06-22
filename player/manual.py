# manual.py
# Desc: Manual CLI for a single game instance.
# Author: Noah Black (noah.black0425@gmail.com)
# Last Updated: June 21st, 2025


# NATIVE IMPORTS.
# THIRD-PARTY IMPORTS.
# LOCAL IMPORTS.
from .base import PlayerInterface
from game.core import GameInstance


# CLASSES.
class ManualPlayer(PlayerInterface):
    def __init__(self):
        super().__init__()

    def select(self, game: GameInstance) -> list[int]:
        print(f"--- ROUND {game.rollCount} ---")
        
        # Print a summary of the board state for the player to view.
        print(self.roundAsStr(game))

        # Prompt the user for which move they would like to select.
        validIndices = [ index for index in range(len(game.validMoves)) ]
        validIndicesAsStr = [ str(index) for index in validIndices ]
        selectedMove = []
        while True:
            moveSelection = input("Select a move: ")
            if moveSelection in validIndicesAsStr:
                moveSelectionAsInt = int(moveSelection)
                selectedMove = game.validMoves[moveSelectionAsInt]
                break
            print("Reponse was not recognized, please try again.")

        # Return the user's selected moves.
        print()
        return selectedMove


# MAIN ENTRY.
def main() -> None:
    raise NotImplementedError

if __name__=="__main__":
    main()
