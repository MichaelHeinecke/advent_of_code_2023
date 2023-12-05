from advent_of_code_2023.day2.cube_conundrum import parse_game, Game


def test_game_is_parsed_correctly():
    game_line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    expected_game = Game(
        game_id=1, max_red_cubes=4, max_green_cubes=2, max_blue_cubes=6
    )

    actual_game = parse_game(game_line)

    assert actual_game == expected_game
