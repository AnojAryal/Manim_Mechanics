from __future__ import annotations

from typing import Optional

from manim import *


class BasicShape(VGroup):
    """Base class for basic shapes with physical properties."""

    def __init__(
        self,
        fill_color: str = BLUE_E,
        fill_opacity: float = 0.5,
        stroke_color: str = WHITE,
        stroke_width: float = 2,
        **kwargs,
    ) -> None:
        self._fill_color = fill_color
        self._fill_opacity = fill_opacity
        self._stroke_color = stroke_color
        self._stroke_width = stroke_width

        super().__init__(**kwargs)


class Square(BasicShape):
    """
    A square with physical dimensions.

    Parameters
    ----------
    side_length:
        Length of each side of the square.

    fill_color:
        Color of the square fill.

    fill_opacity:
        Opacity of the square fill.

    stroke_color:
        Color of the square border.

    stroke_width:
        Width of the square border.
    """

    def __init__(
        self,
        side_length: float = 2.0,
        fill_color: str = BLUE_E,
        fill_opacity: float = 0.5,
        stroke_color: str = WHITE,
        stroke_width: float = 2,
        **kwargs,
    ) -> None:
        self._side_length = side_length

        super().__init__(
            fill_color=fill_color,
            fill_opacity=fill_opacity,
            stroke_color=stroke_color,
            stroke_width=stroke_width,
            **kwargs,
        )

        self.geometry = self._create_geometry()
        self.add(self.geometry)

    def _create_geometry(self) -> Rectangle:
        return Rectangle(
            width=self._side_length,
            height=self._side_length,
            fill_color=self._fill_color,
            fill_opacity=self._fill_opacity,
            stroke_color=self._stroke_color,
            stroke_width=self._stroke_width,
        )


class RectangleShape(BasicShape):
    """
    A rectangle with physical dimensions.

    Parameters
    ----------
    width:
        Width of the rectangle.

    height:
        Height of the rectangle.

    fill_color:
        Color of the rectangle fill.

    fill_opacity:
        Opacity of the rectangle fill.

    stroke_color:
        Color of the rectangle border.

    stroke_width:
        Width of the rectangle border.
    """

    def __init__(
        self,
        width: float = 3.0,
        height: float = 2.0,
        fill_color: str = BLUE_E,
        fill_opacity: float = 0.5,
        stroke_color: str = WHITE,
        stroke_width: float = 2,
        **kwargs,
    ) -> None:
        self._width = width
        self._height = height

        super().__init__(
            fill_color=fill_color,
            fill_opacity=fill_opacity,
            stroke_color=stroke_color,
            stroke_width=stroke_width,
            **kwargs,
        )

        self.geometry = self._create_geometry()
        self.add(self.geometry)

    def _create_geometry(self) -> Rectangle:
        return Rectangle(
            width=self._width,
            height=self._height,
            fill_color=self._fill_color,
            fill_opacity=self._fill_opacity,
            stroke_color=self._stroke_color,
            stroke_width=self._stroke_width,
        )


class CircleShape(BasicShape):
    """
    A circle with physical dimensions.

    Parameters
    ----------
    radius:
        Radius of the circle.

    fill_color:
        Color of the circle fill.

    fill_opacity:
        Opacity of the circle fill.

    stroke_color:
        Color of the circle border.

    stroke_width:
        Width of the circle border.
    """

    def __init__(
        self,
        radius: float = 1.0,
        fill_color: str = BLUE_E,
        fill_opacity: float = 0.5,
        stroke_color: str = WHITE,
        stroke_width: float = 2,
        **kwargs,
    ) -> None:
        self._radius = radius

        super().__init__(
            fill_color=fill_color,
            fill_opacity=fill_opacity,
            stroke_color=stroke_color,
            stroke_width=stroke_width,
            **kwargs,
        )

        self.geometry = self._create_geometry()
        self.add(self.geometry)

    def _create_geometry(self) -> Circle:
        return Circle(
            radius=self._radius,
            fill_color=self._fill_color,
            fill_opacity=self._fill_opacity,
            stroke_color=self._stroke_color,
            stroke_width=self._stroke_width,
        )


class TriangleShape(BasicShape):
    """
    A triangle with physical dimensions.

    Parameters
    ----------
    side_length:
        Length of each side (equilateral triangle).

    fill_color:
        Color of the triangle fill.

    fill_opacity:
        Opacity of the triangle fill.

    stroke_color:
        Color of the triangle border.

    stroke_width:
        Width of the triangle border.
    """

    def __init__(
        self,
        side_length: float = 2.0,
        fill_color: str = BLUE_E,
        fill_opacity: float = 0.5,
        stroke_color: str = WHITE,
        stroke_width: float = 2,
        **kwargs,
    ) -> None:
        self._side_length = side_length

        super().__init__(
            fill_color=fill_color,
            fill_opacity=fill_opacity,
            stroke_color=stroke_color,
            stroke_width=stroke_width,
            **kwargs,
        )

        self.geometry = self._create_geometry()
        self.add(self.geometry)

    def _create_geometry(self) -> Triangle:
        triangle = Triangle(
            fill_color=self._fill_color,
            fill_opacity=self._fill_opacity,
            stroke_color=self._stroke_color,
            stroke_width=self._stroke_width,
        )

        triangle.scale(self._side_length / 2.0)
        return triangle
