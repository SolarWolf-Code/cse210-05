import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.left_snake import Player_1
from game.casting.right_snake import Player_2
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.grow_tail import GrowTail
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():

    # create the cast
    cast = Cast()
    # Left Snake (Player 1)
    left_snake_score = Score("Player One")
    cast.add_actor("left_snake", Player_1())
    cast.add_actor("left_snake_score", left_snake_score)
    left_snake_score.set_position(Point(10, 10))

    # Right Snake (Player 2)
    right_snake_score = Score("Player Two")
    cast.add_actor("right_snake_score", right_snake_score)
    cast.add_actor("right_snake", Player_2())
    right_snake_score.set_position(Point(int(10 + constants.MAX_X/1.2), 10))

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()
    handle_collision = HandleCollisionsAction()

    script = Script()
    script.add_action("input", ControlActorsAction(
        keyboard_service, handle_collision))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", GrowTail(handle_collision))
    script.add_action("update", handle_collision)
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
