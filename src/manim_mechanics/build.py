from manim import *
from manim_mechanics import Mechanics, PointLoad, Support, PhysicalBox, DistributedLoad, MomentLoad
from manim_mechanics import DimensionLine, RectangleShape, TriangleShape, ForceVector, TriangleShape, CircleShape


class CreateBeam(Scene):
    def construct(self):
        # Simple beam - just 3 lines!
        beam = Mechanics(
            length=8,
            supports=[Support(0, "pinned"), Support(8, "roller")],
            point_loads=[PointLoad(4, 10, "down", "10 kN")],
        )
        self.play(Create(beam))
        self.wait()



class MovingObjects(Scene):
    def construct(self):
        # Simple box - fewer parameters
        box = PhysicalBox(width=2, height=1.5, mass=5.0, label="5 kg")
        self.play(Create(box))
        self.wait()
        self.play(box.animate.move_to([0, 1, 0]), run_time=2)
        self.wait()



class ComplexBeam(Scene):
    def construct(self):
        # Complex beam but still simpler syntax
        beam = Mechanics(
            length=12,
            supports=[Support(0, "pinned"), Support(8, "roller"), Support(12, "free")],
            point_loads=[PointLoad(3, 10, "down", "10 kN"), PointLoad(9, 15, "down", "15 kN")],
            distributed_loads=[DistributedLoad(4, 7, 5, "down", "5 kN/m")],
            moment_loads=[MomentLoad(8, 20, "clockwise", "20 kN·m")],
            show_dimensions=True,
        )
        self.play(Create(beam))
        self.wait()


class TestRectangle(Scene):
    def construct(self):
        # Simple rectangle
        rectangle = RectangleShape(width=4, height=2)
        self.play(Create(rectangle))
        self.wait(2)


class TriangleWithForces(Scene):
    def construct(self):
        # Simple triangle with one force
        triangle = TriangleShape(side_length=3)
        force = ForceVector(magnitude=2, direction="down", start_point=[0, 1.5, 0], label="F", color=RED)
        self.play(Create(triangle))
        self.play(Create(force))
        self.wait(2)


# === SIMPLIFIED EXAMPLES ===

class SimpleTriangle(Scene):
    def construct(self):
        # Just 2 lines!
        triangle = TriangleShape(side_length=3)
        self.play(Create(triangle))
        self.wait()


class SimpleBox(Scene):
    def construct(self):
        # Just 2 lines!
        box = PhysicalBox(width=2, height=2, mass=10, label="10 kg")
        self.play(Create(box))
        self.wait()


class SimpleCircle(Scene):
    def construct(self):
        # Just 2 lines!
        circle = CircleShape(radius=1.5)
        self.play(Create(circle))
        self.wait()


class SimpleForce(Scene):
    def construct(self):
        # Just 2 lines!
        force = ForceVector(magnitude=5, direction="up", label="5N", color=RED)
        self.play(Create(force))
        self.wait()