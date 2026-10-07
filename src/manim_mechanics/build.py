from manim import *
from manim_mechanics import Mechanics, PointLoad, Support

class CreateBeam(Scene):
    def construct(self):
        beam = Mechanics(
            length=8,
            height=0.5,
            supports=[
                Support(position=0, type="pinned"),
                Support(position=8, type="roller"),
            ],
            point_loads=[
                PointLoad(
                    position=4,
                    magnitude=10,
                    direction="down",
                    label="10 kN",
                ),
            ],
        )

        self.play(Create(beam))
        self.wait()