# core.py
# Desc: Core classes for starting and interacting with a single game instance.
# Author: Noah Black (noah.black0425@gmail.com)
# Last Updated: June 21st, 2025


# NATIVE IMPORTS.
from random import randint
import itertools
# THIRD-PARTY IMPORTS.
# LOCAL IMPORTS.


# CLASSES.
class GameInstance():
    def __init__(self, tileCount: int = 9) -> None:
        self._isRunning: bool = False
        self._isFinished: bool = False
        self._tileCount: int = tileCount
        self._tiles: list[bool] = []
        self._rollHistory: list[int] = []
        self._moveHistory: list[list[int]] = []
        self._lastRoll: tuple[int, int] = (-1, -1)
        self._validMoves: list[list[int]] = []

    @property
    def running(self) -> bool:
        return self._isRunning
    
    @property
    def finished(self) -> bool:
        return self._isFinished
    
    @property
    def rollCount(self) -> int:
        return len(self._rollHistory)
    
    @property
    def tiles(self) -> list[bool]:
        return self._tiles
    
    @property
    def lastRoll(self) -> tuple[int, int]:
        return self._lastRoll
    
    @property
    def lastRollTotal(self) -> int:
        return sum(self._lastRoll)
    
    @property
    def rollHistory(self) -> list[int]:
        return self._rollHistory
    
    @property
    def moveHistory(self) -> list[list[int]]:
        return self._moveHistory
    
    @property
    def validMoves(self) -> list[list[int]]:
        return self._validMoves
        
    @property
    def score(self) -> int:
        return sum(index + 1 for index, tileIsFlipped in enumerate(self.tiles) if not tileIsFlipped)
    
    def start(self) -> list[list[int]]:
        if self.running:
            raise Exception("Game cannot be started twice.")

        # Set up the available tiles based on the configured tile count.
        self._tiles = [ False ] * self._tileCount
        self._isRunning = True

        # MAKE FIRST MOVE.
        # Handles only the 'roll' portion of a turn and returns result
        return self._makeRoll()

    def tileValues(self) -> list[int]:
        tileList = []
        for tileIndex, tileIsUsed in enumerate(self._tiles):
            if not tileIsUsed:
                tileList.append(tileIndex + 1)

        return tileList
    
    def turn(self, move: list[int]) -> list[list[int]]:
        # Start the turn by applying the prior move.
        self._flipTiles(move)

        # Check if game is complete and handle.
        if self.finished:
            return []

        # Otherwise, make the next roll and return moves.
        else:
            return self._makeRoll()

    def _makeRoll(self) -> list[list[int]]:
        newRoll = self._roll()
        self._rollHistory.append(newRoll)
        validMovesForRoll = self._getValidMovesForRoll(newRoll)
        validMovesRemaining = (len(validMovesForRoll) > 0)
        
        if validMovesRemaining:
            self._validMoves = validMovesForRoll
            return validMovesForRoll
        
        else:
            self._validMoves = []
            self._isFinished = True
            return []
        
    def summaryize(self) -> str:
        if not self.running:
            return (
                f"--- GAME INSTANCE 0x{id(self)} ---\n"
                f"Status:   Not yet started.\n"
                f"Round(s): 0"
            )
        
        elif self.running and not self.finished:
            return (
                f"--- GAME INSTANCE 0x{id(self)} ---\n"
                f"Status:    Running\n"
                f"Round(s):  {self.rollCount}\n"
                f"\n"
                f"Remaining: {', '.join(str(tile) for tile in self.tileValues())}\n"
                f"Last Roll: {self.lastRoll[0]} + {self.lastRoll[1]} (sum of {self.lastRollTotal})\n"
                f"Moves:     {', '.join(str(move) for move in self.moveHistory)}"
            )
        
        else:
            return (
                f"--- GAME INSTANCE 0x{id(self)} ---\n"
                f"Status:    Finished\n"
                f"Score:     {self.score}\n"
                f"Round(s):  {self.rollCount}\n"
                f"\n"
                f"Remaining: {', '.join(str(tile) for tile in self.tileValues())}\n"
                f"Last Roll: {self.lastRoll[0]} + {self.lastRoll[1]} (sum of {self.lastRollTotal})\n"
                f"Moves:     {', '.join(str(move) for move in self.moveHistory)}"
            )
        
    def _flipTiles(self, move: list[int]) -> None:
        if move not in self.validMoves:
            raise Exception(f"Move {move} not a possible move from previous roll {self._rollHistory[-1]}")
        
        for moveTile in move:
            if self._tiles[moveTile - 1] == True:
                raise Exception(f"Cannot flip tile {moveTile} that has already been flipped!")
            self._tiles[moveTile - 1] = True

        self._moveHistory.append(move)
        
        # Check if the game is complete and flag if so.
        gameIsComplete = all(self._tiles)
        if gameIsComplete:
            self._isFinished = True
        return

    def _roll(self) -> int:
        dice1, dice2 = randint(1, 6), randint(1, 6)
        self._lastRoll = (dice1, dice2)
        return dice1 + dice2

    def _getValidMovesForRoll(self, roll: int) -> list[list[int]]:
        # Get the current list of available tiles.
        tileList = self.tileValues()

        # Remove any tiles from the list that are greater in value than the roll.
        tileList = [ tile for tile in tileList if tile <= roll ]

        # Get all combinations of numbers in the tile list.
        # Restricts the length of combos to the max # on a full board.
        tileComboList = []
        for comboLen in range(1, 5):
            combosOfLengthList = itertools.combinations(tileList, comboLen)
            tileComboList.extend([ combo for combo in combosOfLengthList if sum(combo) == roll ])

        # Return the final list of combinations.
        # Make sure to convert all of the values to list representations, instead of tuples returned by combo functions.
        return [ list(combo) for combo in tileComboList ] 


# MAIN ENTRY.
def main() -> None:
    raise NotImplementedError

if __name__=="__main__":
    main()
