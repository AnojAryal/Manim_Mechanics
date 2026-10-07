from manim import *
from manim_mechanics import Mechanics, PointLoad, Support, PhysicalBox, DistributedLoad, MomentLoad
from manim_mechanics import DimensionLine


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



class MovingObjects(Scene):
    def construct(self):
        box = PhysicalBox(
            width=2,
            height=1.5,
            mass=5.0,
            position=[-3, 0, 0],
            label="m = 5 kg",
        )

        self.play(Create(box))
        self.wait()

        # Move to new position
        self.play(box.animate.move_to([0, 1, 0]), run_time=2)
        self.wait()

        # Update mass label
        box.set_mass(10.0)
        self.play(box.animate.move_to([3, 0, 0]), run_time=2)
        self.wait()



class ComplexBeam(Scene):
    def construct(self):
        beam = Mechanics(
            length=12,
            height=0.5,
            supports=[
                Support(position=0, type="pinned"),
                Support(position=8, type="roller"),
                Support(position=12, type="free"),
            ],
            point_loads=[
                PointLoad(position=3, magnitude=10, direction="down", label="10 kN"),
                PointLoad(position=9, magnitude=15, direction="down", label="15 kN"),
            ],
            distributed_loads=[
                DistributedLoad(
                    start_position=4,
                    end_position=7,
                    magnitude=5,
                    direction="down",
                    label="5 kN/m",
                ),
            ],
            moment_loads=[
                MomentLoad(
                    position=8,
                    magnitude=20,
                    direction="clockwise",
                    label="20 kN·m",
                ),
            ],
            show_dimensions=True,
        )

        self.play(Create(beam))
        self.wait()