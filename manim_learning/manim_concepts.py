from manim import *

#create a triangle
class CreateTriangle(Scene):
    def construct(self):
        triangle = Triangle()
        self.play(Create(triangle))
        self.wait()

#create a circle
class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
        self.wait()


#transform two or more shapes into each other
class SquareToCircle(Scene):
    def construct(self):

        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.rotate(PI / 4)

        triangle = Triangle()
        triangle.rotate(-PI / 4)

        self.play(Create(square))
        self.play(Create(triangle))

        self.play(Transform(square, circle))

        self.play(FadeOut(square, triangle))


#transform a square into a circle and then fade out the circle
class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

#transform a sphere into a circle and then fade out the circle
class SphereToCircle(Scene):
    def construct(self):
        sphere = Sphere()
        circle = Circle()

        self.play(Create(sphere))
        self.play(Transform(sphere, circle))
        self.play(FadeOut(sphere))


