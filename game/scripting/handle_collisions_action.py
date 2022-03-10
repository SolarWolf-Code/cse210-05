import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.

    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        left_snake = cast.get_first_actor("left_snake")
        left_snake_head = left_snake.get_segments()[0]
        left_snake_segments = left_snake.get_segments()[1:]

        right_snake = cast.get_first_actor("right_snake")
        right_snake_head = right_snake.get_segments()[0]
        right_snake_segments = right_snake.get_segments()[1:]

        # Player 1 segment handling
        for segment in left_snake_segments:
            if right_snake_head.get_position().equals(segment.get_position()):
                self._is_game_over = True

        # Player 2 segment handling
        for segment in right_snake_segments:
            if left_snake_head.get_position().equals(segment.get_position()):
                self._is_game_over = True

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            left_snake = cast.get_first_actor("left_snake")
            left_snake_segments = left_snake.get_segments()

            right_snake = cast.get_first_actor("right_snake")
            right_snake_segments = right_snake.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in left_snake_segments:
                segment.set_color(constants.WHITE)

            for segment in right_snake_segments:
                segment.set_color(constants.WHITE)

    # function to handle game over condition. Sent to grow_tail.py to prevent tail growth after game over.
    def get_game_over(self):
        return self._is_game_over
