import random

from game.scripting.action import Action
from game.scripting.handle_collisions_action import HandleCollisionsAction


class GrowTail(Action):
    """An update action that grows actors' tails as they move, unless dead."""

    def __init__(self, handle_collision):
        """Initializes GrowTail action."""

        super().__init__()
        self.handle_collision = handle_collision
        self._step = 0

    def execute(self, cast, script):
        """Executes the tail growth action."""

        if not self.handle_collision.get_game_over() and (self._step % 20 == 0):

            left_snake = cast.get_first_actor("left_snake")
            left_snake.grow_tail(1)

            right_snake = cast.get_first_actor("right_snake")
            right_snake.grow_tail(1)

        self._step += 1
