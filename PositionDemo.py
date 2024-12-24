from manimlib import *

class PositionDemo(Scene):

    def construct(self) -> None:
        tl = Text('Top Left')
        top = Text('Top')
        tr = Text('Right')

        center = Text('Center')
        left = Text('Left')
        right = Text('Right')

        dl = Text('Down Left')
        down = Text('Down')
        dr = Text('Down Right')

        bottom = Text('Bottom')
        left_side = Text('Left Side')
        right_side = Text('Right Side')

        bottom.move_to(BOTTOM)
        left_side.move_to(LEFT_SIDE)
        right_side.move_to(RIGHT_SIDE)

        tl.move_to(UL)
        top.move_to(TOP)
        tr.move_to(UR)

        dl.move_to(DL)
        down.move_to(DOWN)
        dr.move_to(DR)

        left.move_to(LEFT)
        right.move_to(RIGHT)

        self.add(tl,top,tr,center,dl,down,dr,bottom,left_side,right_side)

