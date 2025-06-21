# test_game.py
# Desc: Unit tests for the game module.
# Author: Noah Black (noah.black0425@gmail.com)
# Last Updated: June 21st, 2025


# NATIVE IMPORTS.
# THIRD-PARTY IMPORTS.
# LOCAL IMPORTS.
import core


# CONSTANTS.


# STRUCTS.


# FUNCTIONS.


# CLASSES.
class TestCore():
    def test_gameInit(self) -> None:
        game = core.GameInstance()
        assert not game.running
        assert not game.finished
        return

    def test_initialState(self) -> None:
        TILE_COUNT: int = 9
        game = core.GameInstance(tileCount = TILE_COUNT)
        game.new()
        assert game.running
        assert not game.finished
        assert len(game.remainingTiles()) == TILE_COUNT
        return

    def test_getMovesForRoll(self) -> None:
        game = core.GameInstance()
        game.new()

        MAX_ROLL: int = 12
        KNOWN_MAX_ROLL_COMBO_COUNT: int = 12
        maxRollMoves = game._getValidMovesForRoll(MAX_ROLL)
        assert len(maxRollMoves) == KNOWN_MAX_ROLL_COMBO_COUNT

        MIN_ROLL: int = 2
        KNOWN_MIN_ROLL_COMBO_COUNT: int = 1
        minRollMoves = game._getValidMovesForRoll(MIN_ROLL)
        assert len(minRollMoves) == KNOWN_MIN_ROLL_COMBO_COUNT

        invalidRollMoves = game._getValidMovesForRoll(-1)
        assert len(invalidRollMoves) == 0

        return
    
    def test_firstMove(self) -> None:
        game = core.GameInstance()
        assert game.new() != []

    def test_fullGameTerminates(self) -> None:
        game = core.GameInstance()
        moves = game.new()

        MAX_ITERATIONS: int = 20
        iteration: int = 0
        while game.running and not game.finished:
            iteration += 1
            if iteration > MAX_ITERATIONS:
                raise Exception("Game did not terminate past max # of possible iterations!")
            assert moves != []
            moves = game.turn(moves[0])

        return
    
    def test_manyGames(self) -> None:
        GAME_ITERATIONS: int = 500
        for iteration in range(GAME_ITERATIONS):
            try:
                self.test_fullGameTerminates()
            except Exception as e:
                print(f"Failed on iteration {iteration}")
                raise
        return
        
# MAIN ENTRY.
def main() -> None:
    raise NotImplementedError

if __name__=="__main__":
    main()
