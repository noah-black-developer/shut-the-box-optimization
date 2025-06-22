# main.py
# Desc: Main file for the shut-the-box-optimization project.
# Author: Noah Black (noah.black0425@gmail.com)
# Last Updated: June 21st, 2025


# NATIVE IMPORTS.
import argparse
# THIRD-PARTY IMPORTS.
# LOCAL IMPORTS.
import player.manual as manual
import game.core as core


# FUNCTIONS.
def simple(args: argparse.Namespace) -> int:
    """Run a single game with user inputs.

    :return: Return code
    :rtype: int
    """
    manualPlayer = manual.ManualPlayer()
    game = core.GameInstance()

    # Start game loop.
    moveList = game.new()
    while game.running and not game.finished:
        # If no moves are available, force an exit.
        if moveList == []:
            break

        # Select a move and play.
        selectedMove = manualPlayer.select(game)
        moveList = game.turn(selectedMove)

    # Print one final round, then a closing statement.
    print(manualPlayer.roundAsStr(game))
    print("-----------------")
    print("Game is finished!")
    print(f"Final score: {game.score}")
    print("-----------------")

    # Return once game is finished.
    return 0


# MAIN ENTRY.
def main() -> int:
    # SET UP PARSER.
    parser = argparse.ArgumentParser(
        description = "Analyze various players/strategies for the 'Shut the Box' dice game."
    )

    # Add a single subparser for each different run mode.
    subparsers = parser.add_subparsers(help = "Selected run mode.", required = True)
    
    simpleParser = subparsers.add_parser(name = "simple", help = "Configure and run a single game of Shut the Box")
    simpleParser.set_defaults(func = simple)

    # START RUN.
    # Call user selections as a function call, then return results.
    args = parser.parse_args()
    return args.func(args)

if __name__=="__main__":
    exit(main())
