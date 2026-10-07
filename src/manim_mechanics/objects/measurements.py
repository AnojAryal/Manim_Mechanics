from __future__ import annotations

from typing import Optional

from manim import *


class DimensionLine(VGroup):
    """
    A dimension line with arrows and labels.

    This is a higher-level conceptual object for displaying dimensions.
    The user specifies the start and end points, and the visualization
    is handled automatically.

    Parameters
    ----------
    start_point:
        Starting point of the dimension [x, y, z].

    end_point:
        Ending point of the dimension [x, y, z].

    label:
        Label to display for the dimension.

    offset:
        Offset distance from the measured object.

    color:
        Color of the dimension line and text.

    show_arrows:
        Whether to show arrows at the ends.

    arrow_size:
        Size of the arrows.
    """

    def __init__(
        self,
        start_point: list[float],
        end_point: list[float],
        label: str | None = None,
        offset: float = 0.3,
        color: str = WHITE,
        show_arrows: bool = True,
        arrow_size: float = 0.15,
        **kwargs,
    ) -> None:
        self.start_point = start_point
        self.end_point = end_point
        self.label_text = label
        self.offset = offset
        self._color = color
        self.show_arrows = show_arrows
        self.arrow_size = arrow_size

        super().__init__(**kwargs)

        self.line = self._create_line()
        self.arrows = self._create_arrows() if self.show_arrows else VGroup()
        self.label_obj = self._create_label() if self.label_text else VGroup()

        self.add(self.line, self.arrows, self.label_obj)

    def _create_line(self) -> Line:
        """Create the dimension line."""
        midpoint = [
            (self.start_point[0] + self.end_point[0]) / 2,
            (self.start_point[1] + self.end_point[1]) / 2,
            (self.start_point[2] + self.end_point[2]) / 2,
        ]

        direction = [
            self.end_point[0] - self.start_point[0],
            self.end_point[1] - self.start_point[1],
        ]

        length = np.sqrt(direction[0]**2 + direction[1]**2)
        if length == 0:
            return Line(self.start_point, self.end_point, color=self._color)

        perp = [-direction[1] / length, direction[0] / length]

        offset_start = [
            self.start_point[0] + perp[0] * self.offset,
            self.start_point[1] + perp[1] * self.offset,
            self.start_point[2],
        ]

        offset_end = [
            self.end_point[0] + perp[0] * self.offset,
            self.end_point[1] + perp[1] * self.offset,
            self.end_point[2],
        ]

        return Line(offset_start, offset_end, color=self._color, stroke_width=1.5)

    def _create_arrows(self) -> VGroup:
        """Create arrows at the ends of the dimension line."""
        arrows = VGroup()

        direction = [
            self.end_point[0] - self.start_point[0],
            self.end_point[1] - self.start_point[1],
        ]

        length = np.sqrt(direction[0]**2 + direction[1]**2)
        if length == 0:
            return arrows

        perp = [-direction[1] / length, direction[0] / length]

        offset_start = [
            self.start_point[0] + perp[0] * self.offset,
            self.start_point[1] + perp[1] * self.offset,
            self.start_point[2],
        ]

        offset_end = [
            self.end_point[0] + perp[0] * self.offset,
            self.end_point[1] + perp[1] * self.offset,
            self.end_point[2],
        ]

        for point in [offset_start, offset_end]:
            arrow = Arrow(
                start=point,
                end=[point[0] - direction[0] / length * self.arrow_size,
                     point[1] - direction[1] / length * self.arrow_size,
                     point[2]],
                buff=0,
                color=self._color,
                stroke_width=2,
            )
            arrows.add(arrow)

        return arrows

    def _create_label(self) -> MathTex:
        """Create the dimension label."""
        midpoint = [
            (self.start_point[0] + self.end_point[0]) / 2,
            (self.start_point[1] + self.end_point[1]) / 2,
            (self.start_point[2] + self.end_point[2]) / 2,
        ]

        direction = [
            self.end_point[0] - self.start_point[0],
            self.end_point[1] - self.start_point[1],
        ]

        length = np.sqrt(direction[0]**2 + direction[1]**2)
        if length == 0:
            return MathTex(self.label_text, color=self._color)

        perp = [-direction[1] / length, direction[0] / length]

        label_point = [
            midpoint[0] + perp[0] * self.offset,
            midpoint[1] + perp[1] * self.offset,
            midpoint[2],
        ]

        label = MathTex(self.label_text, color=self._color)
        label.move_to(label_point)

        return label


class AngleArc(VGroup):
    """
    An angle arc with label.

    This is a higher-level conceptual object for displaying angles.
    The user specifies the vertex and two points, and the visualization
    is handled automatically.

    Parameters
    ----------
    vertex:
        Vertex point of the angle [x, y, z].

    point1:
        First point defining the angle [x, y, z].

    point2:
        Second point defining the angle [x, y, z].

    label:
        Label to display for the angle.

    radius:
        Radius of the angle arc.

    color:
        Color of the angle arc and text.

    angle_type:
        Type of angle to display ("inner" or "outer").
    """

    def __init__(
        self,
        vertex: list[float],
        point1: list[float],
        point2: list[float],
        label: str | None = None,
        radius: float = 0.5,
        color: str = WHITE,
        angle_type: str = "inner",
        **kwargs,
    ) -> None:
        self.vertex = vertex
        self.point1 = point1
        self.point2 = point2
        self.label_text = label
        self.radius = radius
        self._color = color
        self.angle_type = angle_type

        super().__init__(**kwargs)

        self.arc = self._create_arc()
        self.label_obj = self._create_label() if self.label_text else VGroup()

        self.add(self.arc, self.label_obj)

    def _calculate_angle(self) -> float:
        """Calculate the angle between the two lines."""
        v1 = [
            self.point1[0] - self.vertex[0],
            self.point1[1] - self.vertex[1],
        ]
        v2 = [
            self.point2[0] - self.vertex[0],
            self.point2[1] - self.vertex[1],
        ]

        dot = v1[0] * v2[0] + v1[1] * v2[1]
        mag1 = np.sqrt(v1[0]**2 + v1[1]**2)
        mag2 = np.sqrt(v2[0]**2 + v2[1]**2)

        if mag1 == 0 or mag2 == 0:
            return 0

        cos_angle = dot / (mag1 * mag2)
        cos_angle = max(-1, min(1, cos_angle))
        angle = np.arccos(cos_angle)

        if self.angle_type == "outer":
            angle = 2 * PI - angle

        return angle

    def _calculate_start_angle(self) -> float:
        """Calculate the starting angle for the arc."""
        v1 = [
            self.point1[0] - self.vertex[0],
            self.point1[1] - self.vertex[1],
        ]

        return np.arctan2(v1[1], v1[0])

    def _create_arc(self) -> Arc:
        """Create the angle arc."""
        angle = self._calculate_angle()
        start_angle = self._calculate_start_angle()

        return Arc(
            radius=self.radius,
            angle=angle,
            start_angle=start_angle,
            color=self._color,
            stroke_width=2,
        )

    def _create_label(self) -> MathTex:
        """Create the angle label."""
        angle = self._calculate_angle()
        start_angle = self._calculate_start_angle()

        mid_angle = start_angle + angle / 2

        label_point = [
            self.vertex[0] + self.radius * 1.2 * np.cos(mid_angle),
            self.vertex[1] + self.radius * 1.2 * np.sin(mid_angle),
            self.vertex[2],
        ]

        label = MathTex(self.label_text, color=self._color)
        label.move_to(label_point)

        return label


class ValueLabel(VGroup):
    """
    A value label with optional background.

    This is a higher-level conceptual object for displaying values.
    The user specifies the value and position, and the visualization
    is handled automatically.

    Parameters
    ----------
    value:
        Value to display (can be a string or number).

    position:
        Position of the label [x, y, z].

    color:
        Color of the text.

    background:
        Whether to show a background rectangle.

    background_color:
        Color of the background.

    background_opacity:
        Opacity of the background.
    """

    def __init__(
        self,
        value: str | float,
        position: list[float] | None = None,
        color: str = WHITE,
        background: bool = False,
        background_color: str = BLACK,
        background_opacity: float = 0.7,
        **kwargs,
    ) -> None:
        self.value = str(value)
        self.position = position if position is not None else [0.0, 0.0, 0.0]
        self._color = color
        self.background = background
        self.background_color = background_color
        self.background_opacity = background_opacity

        super().__init__(**kwargs)

        self.text = self._create_text()
        self.bg_rect = self._create_background() if self.background else VGroup()

        self.add(self.bg_rect, self.text)

    def _create_text(self) -> MathTex:
        """Create the text label."""
        text = MathTex(self.value, color=self._color)
        text.move_to(self.position)
        return text

    def _create_background(self) -> Rectangle:
        """Create a background rectangle."""
        bg = Rectangle(
            width=self.text.width + 0.4,
            height=self.text.height + 0.3,
            fill_color=self.background_color,
            fill_opacity=self.background_opacity,
            stroke_width=0,
        )
        bg.move_to(self.position)
        return bg
