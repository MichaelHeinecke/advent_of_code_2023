from dataclasses import dataclass

from advent_of_code_2023.util import get_input_lines


@dataclass
class Game:
    game_id: int
    max_red_cubes: int
    max_green_cubes: int
    max_blue_cubes: int


def parse_game(game_line: str) -> Game:
    game = game_line[5:].split(": ")

    max_colour_cubes = {"red": 0, "green": 0, "blue": 0}
    for raw_draw in game[1].split("; "):
        draws = raw_draw.split(", ")
        for number_colour in draws:
            number_colour = number_colour.split(" ")
            number = int(number_colour[0])
            colour = number_colour[1]
            if number > max_colour_cubes.get(colour):
                max_colour_cubes[colour] = number

    return Game(
        int(game[0]),
        max_colour_cubes["red"],
        max_colour_cubes["green"],
        max_colour_cubes["blue"],
    )


def is_game_possible(
    game: Game,
    number_red_cubes_in_bag: int,
    number_green_cubes_in_bag: int,
    number_blue_cubes_in_bag: int,
) -> bool:
    if (
        game.max_red_cubes <= number_red_cubes_in_bag
        and game.max_green_cubes <= number_green_cubes_in_bag
        and game.max_blue_cubes <= number_blue_cubes_in_bag
    ):
        return True
    else:
        return False


if __name__ == "__main__":
    red_cubes = 12
    green_cubes = 13
    blue_cubes = 14

    games = [parse_game(game_line) for game_line in get_input_lines("games.txt")]
    game_ids = [
        game.game_id
        for game in games
        if is_game_possible(game, red_cubes, green_cubes, blue_cubes)
    ]
    print(f"Sum of possible games: {sum(game_ids)}")

    power_of_cube_set = sum(
        [
            game.max_red_cubes * game.max_green_cubes * game.max_blue_cubes
            for game in games
        ]
    )
    print(f"Power of cube set: {power_of_cube_set}")
