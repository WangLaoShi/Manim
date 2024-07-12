from manimlib import *
class Updater(Scene):
    def construct(self):
        dot = Dot()

        text = TexText("Label").next_to(dot, RIGHT, buff=SMALL_BUFF)

        self.add(dot, text)

        def update_text(obj):
            obj.next_to(dot, RIGHT, buff=SMALL_BUFF)

        # Only works in play
        self.play(
            dot.shift, UP * 2
        )

        self.play(
            UpdateFromFunc(text, update_text)
        )
        self.wait()