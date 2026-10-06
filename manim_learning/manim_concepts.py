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



# create a succession of dots moving to each other's positions
class SuccessionDots(Scene):
    def construct(self):
        dot1 = Dot(point=LEFT * 2 + UP * 2, radius=0.16, color=BLUE)
        dot2 = Dot(point=LEFT * 2 + DOWN * 2, radius=0.16, color=MAROON)
        dot3 = Dot(point=RIGHT * 2 + DOWN * 2, radius=0.16, color=GREEN)
        dot4 = Dot(point=RIGHT * 2 + UP * 2, radius=0.16, color=YELLOW)
        self.add(dot1, dot2, dot3, dot4)

        self.play(Succession(
            dot1.animate.move_to(dot2),
            dot2.animate.move_to(dot3),
            dot3.animate.move_to(dot4),
            dot4.animate.move_to(dot1)
        ))