import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.

    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service, handle_collision):
        """Constructs a new ControlActorsAction using the specified KeyboardService.

        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self.handle_collision = handle_collision
        self._left_snake_direction = Point(0, -constants.CELL_SIZE)
        self._right_snake_direction = Point(0, -constants.CELL_SIZE)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # player 1 left
        if self._keyboard_service.is_key_down('a'):
            original_direction = self._left_snake_direction
            self._left_snake_direction = Point(-constants.CELL_SIZE, 0)

            if (not self.handle_collision.get_game_over()
                and not self._left_snake_direction.equals(original_direction)
                and self._keyboard_service.is_key_up('d')
                and self._keyboard_service.is_key_up('s')
                    and self._keyboard_service.is_key_up('w')):
                cast.get_first_actor("left_snake_score").add_points(1)

        # player 1 right
        if self._keyboard_service.is_key_down('d'):
            original_direction = self._left_snake_direction
            self._left_snake_direction = Point(constants.CELL_SIZE, 0)

            if (not self.handle_collision.get_game_over()
                and not self._left_snake_direction.equals(original_direction)
                and self._keyboard_service.is_key_up('a')
                and self._keyboard_service.is_key_up('s')
                    and self._keyboard_service.is_key_up('w')):
                cast.get_first_actor("left_snake_score").add_points(1)

        # player 1 up
        if self._keyboard_service.is_key_down('w'):
            original_direction = self._left_snake_direction
            self._left_snake_direction = Point(0, -constants.CELL_SIZE)

            if (not self.handle_collision.get_game_over()
                and not self._left_snake_direction.equals(original_direction)
                and self._keyboard_service.is_key_up('d')
                and self._keyboard_service.is_key_up('s')
                    and self._keyboard_service.is_key_up('a')):
                cast.get_first_actor("left_snake_score").add_points(1)

        # player 1 down
        if self._keyboard_service.is_key_down('s'):
            original_direction = self._left_snake_direction
            self._left_snake_direction = Point(0, constants.CELL_SIZE)

            if (not self.handle_collision.get_game_over()
                and not self._left_snake_direction.equals(original_direction)
                and self._keyboard_service.is_key_up('d')
                and self._keyboard_service.is_key_up('a')
                    and self._keyboard_service.is_key_up('w')):
                cast.get_first_actor("left_snake_score").add_points(1)

        # player 2 left
        if self._keyboard_service.is_key_down('j'):
            original_direction = self._right_snake_direction
            self._right_snake_direction = Point(-constants.CELL_SIZE, 0)

            if (not self.handle_collision.get_game_over()
                and not self._right_snake_direction.equals(original_direction)
                and self._keyboard_service.is_key_up('l')
                and self._keyboard_service.is_key_up('i')
                    and self._keyboard_service.is_key_up('k')):
                cast.get_first_actor("right_snake_score").add_points(1)

        # player 2 right
        if self._keyboard_service.is_key_down('l'):
            original_direction = self._right_snake_direction
            self._right_snake_direction = Point(constants.CELL_SIZE, 0)

            if (not self.handle_collision.get_game_over()
                and not self._right_snake_direction.equals(original_direction)
                and self._keyboard_service.is_key_up('j')
                and self._keyboard_service.is_key_up('i')
                    and self._keyboard_service.is_key_up('k')):
                cast.get_first_actor("right_snake_score").add_points(1)

        # player 2 up
        if self._keyboard_service.is_key_down('i'):
            original_direction = self._right_snake_direction
            self._right_snake_direction = Point(0, -constants.CELL_SIZE)

            if (not self.handle_collision.get_game_over()
                and not self._right_snake_direction.equals(original_direction)
                and self._keyboard_service.is_key_up('l')
                and self._keyboard_service.is_key_up('j')
                    and self._keyboard_service.is_key_up('k')):
                cast.get_first_actor("right_snake_score").add_points(1)

        # player 2 down
        if self._keyboard_service.is_key_down('k'):
            original_direction = self._right_snake_direction
            self._right_snake_direction = Point(0, constants.CELL_SIZE)

            if (not self.handle_collision.get_game_over()
                and not self._right_snake_direction.equals(original_direction)
                and self._keyboard_service.is_key_up('l')
                and self._keyboard_service.is_key_up('i')
                    and self._keyboard_service.is_key_up('j')):
                cast.get_first_actor("right_snake_score").add_points(1)

        left_snake = cast.get_first_actor("left_snake")
        left_snake.turn_head(self._left_snake_direction)

        right_snake = cast.get_first_actor("right_snake")
        right_snake.turn_head(self._right_snake_direction)
