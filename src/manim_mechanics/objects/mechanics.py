from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Optional

from manim import *


@dataclass
class PointLoad:
    """A point load applied to a beam or structure.

    Simple usage: PointLoad(position, magnitude, direction, label)
    """
    position: float
    magnitude: float
    direction: Literal["up", "down", "left", "right"] = "down"
    label: str | None = None
    color: str = "white"

    def __init__(self, position, magnitude, direction="down", label=None, color="white"):
        self.position = position
        self.magnitude = magnitude
        self.direction = direction
        self.label = label
        self.color = color


@dataclass
class DistributedLoad:
    """A distributed load applied over a segment of a beam."""
    start_position: float
    end_position: float
    magnitude: float
    direction: Literal["up", "down"] = "down"
    label: str | None = None
    color: str = "white"


@dataclass
class MomentLoad:
    """A moment load applied at a specific position."""
    position: float
    magnitude: float
    direction: Literal["clockwise", "counterclockwise"] = "clockwise"
    label: str | None = None
    color: str = "white"


@dataclass
class Support:
    """A support constraint for a beam or structure.

    Simple usage: Support(position, type)
    """
    position: float
    type: Literal["pinned", "roller", "fixed", "free"]

    def __init__(self, position, type):
        self.position = position
        self.type = type


class Mechanics(VGroup):
    """
    A conceptual mechanics beam.

    The Beam is responsible for constructing the Manim objects required
    to visualize its mechanical representation.

    Parameters
    ----------
    length:
        Physical length of the beam.

    height:
        Visual height of the beam.

    supports:
        Supports attached to the beam.

    point_loads:
        Point loads applied to the beam.

    distributed_loads:
        Distributed loads applied over beam segments.

    moment_loads:
        Moment loads applied at specific positions.

    show_dimensions:
        Whether to show dimension labels on the beam.

    dimension_color:
        Color for dimension labels.
    """

    def __init__(
        self,
        length: float,
        height: float = 0.5,
        *,
        supports: list[Support] | None = None,
        point_loads: list[PointLoad] | None = None,
        distributed_loads: list[DistributedLoad] | None = None,
        moment_loads: list[MomentLoad] | None = None,
        show_dimensions: bool = False,
        dimension_color: str = WHITE,
        **kwargs,
    ) -> None:
        self.beam_length = length
        self.beam_height = height
        self.supports = supports or []
        self.point_loads = point_loads or []
        self.distributed_loads = distributed_loads or []
        self.moment_loads = moment_loads or []
        self.show_dimensions = show_dimensions
        self.dimension_color = dimension_color

        self._validate()

        super().__init__(**kwargs)

        self.geometry = self._create_geometry()
        self.support_objects = self._create_supports()
        self.point_load_objects = self._create_point_loads()
        self.distributed_load_objects = self._create_distributed_loads()
        self.moment_load_objects = self._create_moment_loads()
        self.dimension_objects = self._create_dimensions() if show_dimensions else VGroup()

        self.add(
            self.geometry,
            self.support_objects,
            self.point_load_objects,
            self.distributed_load_objects,
            self.moment_load_objects,
            self.dimension_objects,
        )

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    def _validate(self) -> None:
        if self.beam_length <= 0:
            raise ValueError(
                "Beam length must be greater than zero."
            )

        if self.beam_height <= 0:
            raise ValueError(
                "Beam height must be greater than zero."
            )

        for support in self.supports:
            self._validate_position(support.position)

        for load in self.point_loads:
            self._validate_position(load.position)

        for load in self.distributed_loads:
            self._validate_position(load.start_position)
            self._validate_position(load.end_position)
            if load.start_position >= load.end_position:
                raise ValueError(
                    f"Distributed load start position {load.start_position} "
                    f"must be less than end position {load.end_position}."
                )

        for load in self.moment_loads:
            self._validate_position(load.position)

    def _validate_position(self, position: float) -> None:
        if not 0 <= position <= self.beam_length:
            raise ValueError(
                f"Position {position} must be between "
                f"0 and {self.beam_length}."
            )

    # ------------------------------------------------------------------
    # Geometry
    # ------------------------------------------------------------------

    def _create_geometry(self) -> Rectangle:
        return Rectangle(
            width=self.beam_length,
            height=self.beam_height,
            stroke_color=WHITE,
            stroke_width=2,
            fill_color=BLUE_E,
            fill_opacity=0.3,
        )

    # ------------------------------------------------------------------
    # Supports
    # ------------------------------------------------------------------

    def _create_supports(self) -> VGroup:
        supports = VGroup()

        for support in self.supports:
            x = self._position_to_x(support.position)

            if support.type == "pinned":
                support_group = self._create_pinned_support(x)
            elif support.type == "roller":
                support_group = self._create_roller_support(x)
            elif support.type == "fixed":
                support_group = self._create_fixed_support(x)
            elif support.type == "free":
                support_group = VGroup()
            else:
                raise ValueError(
                    f"Unsupported support type: {support.type}"
                )

            supports.add(support_group)

        return supports

    def _create_pinned_support(self, x: float) -> VGroup:
        triangle = Triangle(
            fill_color=WHITE,
            fill_opacity=1,
            stroke_color=WHITE,
        )

        triangle.scale(0.35)
        triangle.rotate(PI)
        triangle.move_to(
            [x, -self.beam_height / 2 - 0.25, 0]
        )

        ground_line = Line(
            [x - 0.6, -self.beam_height / 2 - 0.55, 0],
            [x + 0.6, -self.beam_height / 2 - 0.55, 0],
            stroke_color=WHITE,
            stroke_width=2,
        )

        return VGroup(triangle, ground_line)

    def _create_roller_support(self, x: float) -> VGroup:
        triangle = Triangle(
            fill_color=WHITE,
            fill_opacity=1,
            stroke_color=WHITE,
        )

        triangle.scale(0.35)
        triangle.rotate(PI)
        triangle.move_to(
            [x, -self.beam_height / 2 - 0.25, 0]
        )

        wheel_left = Circle(
            radius=0.12,
            fill_color=WHITE,
            fill_opacity=1,
            stroke_color=WHITE,
        )

        wheel_right = Circle(
            radius=0.12,
            fill_color=WHITE,
            fill_opacity=1,
            stroke_color=WHITE,
        )

        wheel_left.move_to(
            [x - 0.15, -self.beam_height / 2 - 0.55, 0]
        )

        wheel_right.move_to(
            [x + 0.15, -self.beam_height / 2 - 0.55, 0]
        )

        ground_line = Line(
            [x - 0.6, -self.beam_height / 2 - 0.7, 0],
            [x + 0.6, -self.beam_height / 2 - 0.7, 0],
            stroke_color=WHITE,
            stroke_width=2,
        )

        return VGroup(
            triangle,
            wheel_left,
            wheel_right,
            ground_line,
        )

    def _create_fixed_support(self, x: float) -> VGroup:
        rect = Rectangle(
            width=0.4,
            height=0.6,
            fill_color=WHITE,
            fill_opacity=1,
            stroke_color=WHITE,
        )

        rect.move_to(
            [x, -self.beam_height / 2 - 0.35, 0]
        )

        hatch_lines = VGroup()
        for i in range(5):
            line = Line(
                [x - 0.2 + i * 0.1, -self.beam_height / 2 - 0.05, 0],
                [x - 0.15 + i * 0.1, -self.beam_height / 2 - 0.65, 0],
                stroke_color=WHITE,
                stroke_width=1,
            )
            hatch_lines.add(line)

        ground_line = Line(
            [x - 0.6, -self.beam_height / 2 - 0.75, 0],
            [x + 0.6, -self.beam_height / 2 - 0.75, 0],
            stroke_color=WHITE,
            stroke_width=2,
        )

        return VGroup(rect, hatch_lines, ground_line)

    # ------------------------------------------------------------------
    # Loads
    # ------------------------------------------------------------------

    def _create_point_loads(self) -> VGroup:
        loads = VGroup()

        for load in self.point_loads:
            load_group = self._create_point_load(load)
            loads.add(load_group)

        return loads

    def _create_point_load(self, load: PointLoad) -> VGroup:
        x = self._position_to_x(load.position)

        arrow_length = 1.0

        if load.direction == "down":
            start = [
                x,
                self.beam_height / 2 + arrow_length,
                0,
            ]
            end = [
                x,
                self.beam_height / 2,
                0,
            ]
            label_direction = UP
        elif load.direction == "up":
            start = [
                x,
                -self.beam_height / 2 - arrow_length,
                0,
            ]
            end = [
                x,
                -self.beam_height / 2,
                0,
            ]
            label_direction = DOWN
        elif load.direction == "left":
            start = [
                x + arrow_length,
                0,
                0,
            ]
            end = [
                x,
                0,
                0,
            ]
            label_direction = RIGHT
        elif load.direction == "right":
            start = [
                x - arrow_length,
                0,
                0,
            ]
            end = [
                x,
                0,
                0,
            ]
            label_direction = LEFT
        else:
            raise ValueError(f"Unknown direction: {load.direction}")

        arrow = Arrow(
            start=start,
            end=end,
            buff=0,
            color=load._color if hasattr(load, '_color') else load.color,
            stroke_width=4,
        )

        if load.label is not None:
            label = MathTex(load.label, color=load._color if hasattr(load, '_color') else load.color)
            label.next_to(arrow, label_direction)
            return VGroup(arrow, label)

        return VGroup(arrow)

    def _create_distributed_loads(self) -> VGroup:
        loads = VGroup()

        for load in self.distributed_loads:
            load_group = self._create_distributed_load(load)
            loads.add(load_group)

        return loads

    def _create_distributed_load(self, load: DistributedLoad) -> VGroup:
        start_x = self._position_to_x(load.start_position)
        end_x = self._position_to_x(load.end_position)

        arrow_length = 0.8
        num_arrows = max(3, int((end_x - start_x) / 0.5))

        arrows = VGroup()

        for i in range(num_arrows):
            t = i / (num_arrows - 1) if num_arrows > 1 else 0.5
            x = start_x + t * (end_x - start_x)

            if load.direction == "down":
                start = [x, self.beam_height / 2 + arrow_length, 0]
                end = [x, self.beam_height / 2, 0]
            else:
                start = [x, -self.beam_height / 2 - arrow_length, 0]
                end = [x, -self.beam_height / 2, 0]

            arrow = Arrow(
                start=start,
                end=end,
                buff=0,
                color=load._color if hasattr(load, '_color') else load.color,
                stroke_width=3,
            )
            arrows.add(arrow)

        if load.label is not None:
            label = MathTex(load.label, color=load._color if hasattr(load, '_color') else load.color)
            if load.direction == "down":
                label.next_to(arrows, UP)
            else:
                label.next_to(arrows, DOWN)
            return VGroup(arrows, label)

        return arrows

    def _create_moment_loads(self) -> VGroup:
        loads = VGroup()

        for load in self.moment_loads:
            load_group = self._create_moment_load(load)
            loads.add(load_group)

        return loads

    def _create_moment_load(self, load: MomentLoad) -> VGroup:
        x = self._position_to_x(load.position)

        radius = 0.4
        arc = Arc(
            radius=radius,
            angle=PI / 2,
            color=load._color if hasattr(load, '_color') else load.color,
            stroke_width=3,
        )

        if load.direction == "clockwise":
            arc.rotate(-PI / 4)
            arrow_tip = Arrow(
                start=arc.point_from_proportion(0.9),
                end=arc.point_from_proportion(1.0),
                buff=0,
                color=load._color if hasattr(load, '_color') else load.color,
                stroke_width=3,
            )
        else:
            arc.rotate(PI / 4)
            arc.flip(RIGHT)
            arrow_tip = Arrow(
                start=arc.point_from_proportion(0.9),
                end=arc.point_from_proportion(1.0),
                buff=0,
                color=load._color if hasattr(load, '_color') else load.color,
                stroke_width=3,
            )

        arc.move_to([x, 0, 0])
        arrow_tip.move_to([x, 0, 0])

        if load.label is not None:
            label = MathTex(load.label, color=load._color if hasattr(load, '_color') else load.color)
            label.next_to(arc, UP)
            return VGroup(arc, arrow_tip, label)

        return VGroup(arc, arrow_tip)

    # ------------------------------------------------------------------
    # Dimensions
    # ------------------------------------------------------------------

    def _create_dimensions(self) -> VGroup:
        dimensions = VGroup()

        left_label = MathTex("0", color=self.dimension_color)
        left_label.next_to(
            self.geometry,
            DOWN,
            buff=0.3,
        )
        left_label.align_to(self.geometry, LEFT)

        right_label = MathTex(f"{self.beam_length:g}", color=self.dimension_color)
        right_label.next_to(
            self.geometry,
            DOWN,
            buff=0.3,
        )
        right_label.align_to(self.geometry, RIGHT)

        dimension_line = Line(
            self.geometry.get_left() + DOWN * 0.3,
            self.geometry.get_right() + DOWN * 0.3,
            color=self.dimension_color,
            stroke_width=1,
        )

        dimensions.add(left_label, right_label, dimension_line)

        return dimensions

    # ------------------------------------------------------------------
    # Coordinate conversion
    # ------------------------------------------------------------------

    def _position_to_x(self, position: float) -> float:
        """
        Convert a physical beam position into a Manim x-coordinate.
        """
        return position - self.beam_length / 2