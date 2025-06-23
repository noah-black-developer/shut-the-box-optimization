# main.py
# Desc: Main file for the shut-the-box-optimization project.
# Author: Noah Black (noah.black0425@gmail.com)
# Last Updated: June 21st, 2025


import argparse
from typing import Generator, Type
# THIRD-PARTY IMPORTS.
import tqdm
# LOCAL IMPORTS.
import player
import game.core as core
# NATIVE IMPORTS.


# CONSTANTS.
DEFAULT_ITERATIONS: int = 100000
PLAYER_TYPES: dict[str, Type[player.PlayerInterface]] = {
    "manual":                player.ManualPlayer,
    "random":                player.RandomPlayer,
    "largest-first":         player.LargestFirstPlayer,
    "largest-preserve-low":  player.LargePreserveLowPlayer,
    "most-then-small":       player.MostThenSmall,
    "most-then-large":       player.MostThenLarge,
}


# FUNCTIONS.
def runGame(player: player.PlayerInterface, **gameKwargs) -> core.GameInstance:
    # Instantiate a new game using provided args.
    newGame = core.GameInstance(**gameKwargs)

    # Run the game until finished.
    moveList = newGame.start()
    while newGame.running and not newGame.finished:
        # If no moves are available, force an exit.
        if moveList == []:
            break

        # Select a move and play.
        selectedMove = player.select(newGame)
        moveList = newGame.turn(selectedMove)
    
    # Return the completed game object.
    return newGame

def runGameIterator(playerClass: Type[player.PlayerInterface], limit: int | None = None, **gameKwargs) -> Generator[core.GameInstance, None, None]:
    # Initialize the player used during runs.
    runPlayer = playerClass()

    # Run game iterations and yield each resulting game.
    iteration = 0
    while True:
        if iteration == limit:
            return
        yield runGame(runPlayer, **gameKwargs)
        iteration += 1

def selectPlayer(specifiedPlayer: str | None = None) -> Type[player.PlayerInterface]:
    # If given from function inputs, verify specified player.
    if specifiedPlayer != None:
        # Make sure that the given player matches an expected value.
        if specifiedPlayer not in PLAYER_TYPES.keys():
            raise Exception(f"Specified player name {specifiedPlayer} does not match valid options: {', '.join(PLAYER_TYPES)}")

    # Otherwise, prompt the user to select a player from the available options.
    else:
        print("Please select a player.")
        print("Available options:")
        for playerIndex, playerName in enumerate(PLAYER_TYPES):
            print(f"  [{playerIndex}] {playerName}")
        print()

        validIndicesAsStr = [ str(index) for index in range(0, len(PLAYER_TYPES)) ]
        while True:
            userResponse = input("Enter here: ")
            if userResponse in validIndicesAsStr:
                specifiedPlayer = userResponse
                break
            print("Response was not recognized, please try again.")
        print()

    # Convert selections to the correct player class.
    try:
        gamePlayer = PLAYER_TYPES[specifiedPlayer]
    except:
        raise Exception(f"Unsupported player was selected: {specifiedPlayer}.")
        
    return gamePlayer

def simple(**kwargs) -> int:
    """Run a single game with user-specified player.

    :param **kwargs: Command line arguments
    :type: dict
    :return: Return code
    :rtype: int
    """
    # Run a single game and store the resulting game object.
    playerClass = selectPlayer(kwargs.get("player", None))
    gamePlayer = playerClass()
    game = runGame(gamePlayer)

    # Print one final round, if required, then a round summary.
    if isinstance(gamePlayer, player.ManualPlayer):
        print(gamePlayer.roundAsStr(game))
    print(game.summaryize())

    # Return once game is finished.
    return 0

def iterate(**kwargs) -> int:
    """Run continuous games until a successful game is reached.

    :param **kwargs: Command line arguments
    :type: dict
    :return: Return code
    :rtype: int
    """
    # Select the player type to use.
    playerClass = selectPlayer(kwargs.get("player", None))

    # Start an iterator for continuous games.
    print("Starting games...")
    for gameIndex, game in enumerate(runGameIterator(playerClass)):
        # Check if the current game was successful. If so, break from the loop.
        if game.finished and game.score == 0:
            break

    # Print results.
    print("A successful game was found!")
    print(f"Total iteration(s): {gameIndex + 1}")
    print()
    print(game.summaryize())

    # Return once complete.
    return 0

def run(**kwargs) -> int:
    """Run a specified player for a full number of iterations and tracking results.

    :param **kwargs: Command line arguments
    :type: dict
    :return: Return code
    :rtype: int
    """
    # Get the # of iterations from provided args.
    iterations = kwargs.get("number", DEFAULT_ITERATIONS)

    # Propmt the user to select the player they want to use.
    playerClass = selectPlayer(kwargs.get("player", None))

    # Start iterating and store all results.
    print(f"Running {iterations} games...")
    totalScore = 0
    perfectGames = 0
    for game in tqdm.tqdm(runGameIterator(playerClass, limit = iterations), total = iterations):
        totalScore += game.score
        if game.score == 0:
            perfectGames += 1
    
    print("Analyzing games...")
    avgScore = totalScore / iterations

    # Print an analysis of the completed games.
    print("Run completed!")
    print()
    print(f"Player used: {playerClass.__name__}")
    print(f"Average score: {avgScore:.2f}")
    print(f"Perfect games: {perfectGames}/{iterations} ({(perfectGames/iterations) * 100:.2f}%)")

    # Return once complete.
    return 0

def compare(**kwargs) -> int:
    """Run each non-manual player and compare.

    :param **kwargs: Command line arguments
    :type: dict
    :return: Return code
    :rtype: int
    """
    # Get the # of iterations from provided args.
    iterations = kwargs.get("number", DEFAULT_ITERATIONS)

    # Initialize player fields.
    totalScoreDict = {}
    perfectGamesDict = {}
    for playerName in PLAYER_TYPES.keys():
        if playerName == "manual":
            continue
        totalScoreDict[playerName] = 0
        perfectGamesDict[playerName] = 0

    # Iterate over all player types and respective classes.
    print("Running games for all player types...")
    print()
    for playerName, playerClass in PLAYER_TYPES.items():
        # If this player is manual, skip it.
        if playerName == "manual":
            continue
            
        # Run games with the current player for all iterations.
        print(f"Running player {playerClass.__name__}")
        for game in tqdm.tqdm(runGameIterator(playerClass, limit = iterations), total = iterations):
            totalScoreDict[playerName] += game.score
            if game.score == 0:
                perfectGamesDict[playerName] += 1

    # Once complete, print table of results.
    print("Runs complete!")
    print()
    COLUMNS = [ "Player", "Avg. Score", "Perfect Games", "Perfect Game %" ]
    print(f"{COLUMNS[0]:<25} {COLUMNS[1]:<25} {COLUMNS[2]:<25} {COLUMNS[3]:<25}")
    print("-" * 110)
    for playerName in totalScoreDict.keys():
        # Determine player stats + format.
        avgScore = totalScoreDict[playerName] / iterations
        avgScoreAsStr = f"{avgScore:.2f}"
        perfGameCount = perfectGamesDict[playerName]
        perfGamePercent = (perfGameCount / iterations) * 100
        perfGamePercentAsStr = f"{perfGamePercent:.2f}" + "%"

        # Print new table row.
        print(f"{playerName:<25} {avgScoreAsStr:<25} {str(perfGameCount):<25} {perfGamePercentAsStr:<25}")

    # Return once complete.
    return 0

# MAIN ENTRY.
def main() -> int:
    # SET UP PARSER.
    parser = argparse.ArgumentParser(
        description = "Analyze various players/strategies for the 'Shut the Box' dice game."
    )

    # Add any global arguments here.
    parser.add_argument("-p", "--player", action = "store", default = None, help = "Select a player by name. Skips user prompts.")

    # Add a single subparser for each different run mode.
    subparsers = parser.add_subparsers(help = "Selected run mode.", required = True)
    
    simpleParser = subparsers.add_parser(name = "simple", help = "Configure and run a single game.")
    simpleParser.set_defaults(func = simple)
    
    iterParser = subparsers.add_parser(name = "iterate", help = "Run continuously until a maximum score is reached.")
    iterParser.set_defaults(func = iterate)
    
    runParser = subparsers.add_parser(name = "run", help = "Run a single player for a specified number of iterations.")
    runParser.add_argument("-n", "--number", action = "store", type = int, default = DEFAULT_ITERATIONS, help = "Number of iterations.")
    runParser.set_defaults(func = run)
    
    compareParser = subparsers.add_parser(name = "compare", help = "Run every non-manual player type for a number of iterations, then compare.")
    compareParser.add_argument("-n", "--number", action = "store", type = int, default = DEFAULT_ITERATIONS, help = "Number of iterations.")
    compareParser.set_defaults(func = compare)

    # START RUN.
    # Call user selections as a function call, then return results.
    args = parser.parse_args()
    argsAsDict = vars(args)
    return args.func(**argsAsDict)

if __name__=="__main__":
    exit(main())
