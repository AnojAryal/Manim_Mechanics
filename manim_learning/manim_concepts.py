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


#create square and circle
class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle() 
        circle.set_fill(PINK, opacity=0.5) 

        square = Square() 
        square.set_fill(BLUE, opacity=0.5)

        square.next_to(circle, RIGHT, buff=0.5)  
        self.play(Create(circle), Create(square)) 


#rotate a square in different directions
class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()