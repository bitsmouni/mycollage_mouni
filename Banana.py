class MonkeyBananaProblem:
    def __init__(self):
        self.monkey_height = 0
        self.box_position = 0
        self.banana_height = 3
        self.box_height = 1

    def can_reach_banana(self):
        # Check if the monkey's height is enough to reach the banana
        return self.monkey_height >= self.banana_height

    def move_box(self):
        # Move the box closer to the banana
        if self.box_position < self.banana_height - 1:
            self.box_position += 1
            print(f"Box moved to position: {self.box_position}")
        else:
            print("Box is now directly under the banana.")

    def climb_box(self):
        # The monkey climbs the box to increase its height
        self.monkey_height = self.box_position + self.box_height
        print(f"Monkey climbs box! Current height: {self.monkey_height}")

    def attempt_to_get_banana(self):
        # If the monkey cannot reach the banana, move the box and try again
        if not self.can_reach_banana():
            print("Monkey cannot reach the banana. Moving the box.")
            self.move_box()

            # Once the box is directly under the banana, the monkey climbs it
            if self.box_position == self.banana_height - 1:
                self.climb_box()

            # After climbing, attempt again to reach the banana
            self.attempt_to_get_banana()
        else:
            print("Monkey has reached the banana and got it!")

problem = MonkeyBananaProblem()
problem.attempt_to_get_banana()
