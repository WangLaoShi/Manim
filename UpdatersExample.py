from manimlib import *

class UpdatersExample(Scene):
    """
    This class demonstrates the use of updaters in Manim, a mathematical animation engine.
    Updaters are functions that are called every frame to update the state of an object.
    """

    def construct(self):
        """
        This method constructs the animation scene.
        """

        # Create a square and fill it with blue color
        square = Square()
        square.set_fill(BLUE_E, 1)

        # Create a brace that always redraws itself on top of the square
        brace = always_redraw(Brace, square, UP)

        # Create a label consisting of a text and a decimal number
        text, number = label = VGroup(
            Text("Width = "),
            DecimalNumber(
                0,
                show_ellipsis=True,
                num_decimal_places=2,
                include_sign=True,
            )
        )
        # The RIGHT argument indicates the direction in which the elements of the
        # VGroup should be arranged. In this case, the Text object ("Width = ")
        # will be placed to the left and the DecimalNumber object (initially 0)
        # will be placed to the right. This creates a label that reads "Width = 0"
        # with the number on the right side of the equals sign.  The arrange method
        # is a convenient way to automatically position related elements in a scene
        # without having to manually calculate and set their positions.
        label.arrange(RIGHT)

        # Make the label always appear above the brace
        always(label.next_to, brace, UP)

        # Make the number in the label always equal to the width of the square
        f_always(number.set_value, square.get_width)

        # Add the square, brace, and label to the scene
        self.add(square, brace, label)

        # Animate the square to scale up and down
        # In this context, rate_func is a parameter that determines the rate at
        # which the animation progresses. Different rate functions can be used to
        # create different effects. The there_and_back rate function used here is
        # a predefined function in Manim that makes the animation progress forward
        # and then backward, creating a back-and-forth effect.  The square.animate.scale(2)
        # part of the code is the animation that's being played. It scales the size of a
        # square object by a factor of 2. The rate_func=there_and_back makes this scaling
        # go from the original size to double size and then back to the original size.
        self.play(
            square.animate.scale(2),
            rate_func=there_and_back,
            run_time=2,
        )
        self.wait()

        # Animate the square to stretch its width to 5
        self.play(
            square.animate.set_width(5, stretch=True),
            run_time=3,
        )
        self.wait()

        # Animate the square to set its width back to 2
        self.play(
            square.animate.set_width(2),
            run_time=3
        )
        self.wait()

        # Record the current time and the current width of the square
        now = self.time
        w0 = square.get_width()

        # Add an updater to the square that makes its width oscillate
        square.add_updater(
            lambda m: m.set_width(w0 * math.sin(self.time - now) + w0)
        )

        # Wait for 4 PI seconds
        self.wait(4 * PI)
