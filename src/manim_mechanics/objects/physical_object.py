from __future__ import annotations

from typing import Optional

from manim import *
from .shapes import BasicShape


class PhysicalObject(BasicShape):
    """
    A physical object with mass, position, and dimensions.

    This is a higher-level conceptual object that represents a physical
    entity with properties like mass, position, and dimensions. The
    underlying Manim geometry is handled automatically.

    Parameters
    ----------
    mass:
        Mass of the object (for display and calculations).

    position:
        Initial position of the object [x, y, z].

    velocity:
        Initial velocity vector [vx, vy, vz].

    label:
        Optional label to display with the object.

    show_label:
        Whether to show the label.

    label_position:
        Position of the label relative to the object (UP, DOWN, LEFT, RIGHT).

    fill_color:
        Color of the object fill.

    fill_opacity:
        Opacity of the object fill.

    stroke_color:
        Color of the object border.

    stroke_width:
        Width of the object border.
    """

    def __init__(
        self,
        mass: float = 1.0,
        position: list[float] | None = None,
        velocity: list[float] | None = None,
        label: str | None = None,
        show_label: bool = True,
        label_position: str = UP,
        fill_color: str = BLUE_E,
        fill_opacity: float = 0.5,
        stroke_color: str = WHITE,
        stroke_width: float = 2,
        **kwargs,
    ) -> None:
        self.mass = mass
        self.position = position if position is not None else [0.0, 0.0, 0.0]
        self.velocity = velocity if velocity is not None else [0.0, 0.0, 0.0]
        self.label_text = label
        self.show_label = show_label
        self.label_position = label_position

        super().__init__(
            fill_color=fill_color,
            fill_opacity=fill_opacity,
            stroke_color=stroke_color,
            stroke_width=stroke_width,
            **kwargs,
        )

        self.geometry = self._create_geometry()
        self.label_obj = self._create_label() if self.show_label and self.label_text else VGroup()

        self.add(self.geometry, self.label_obj)

        if self.position:
            self.move_to(self.position)

    def _create_geometry(self) -> VGroup:
        """Override in subclasses to create specific geometry."""
        return VGroup()

    def _create_label(self) -> MathTex:
        """Create a label for the object."""
        if self.label_text:
            label = MathTex(self.label_text)
            label.next_to(self.geometry, self.label_position, buff=0.3)
            return label
        return MathTex("")

    def set_mass(self, mass: float) -> None:
        """Update the mass of the object."""
        self.mass = mass

    def set_position(self, position: list[float]) -> None:
        """Update the position of the object."""
        self.position = position
        self.move_to(position)

    def set_velocity(self, velocity: list[float]) -> None:
        """Update the velocity of the object."""
        self.velocity = velocity


class PhysicalBox(PhysicalObject):
    """
    A physical box (rectangular prism in 2D).

    Parameters
    ----------
    width:
        Width of the box.

    height:
        Height of the box.

    mass:
        Mass of the object.

    position:
        Initial position of the object.

    velocity:
        Initial velocity vector.

    label:
        Optional label to display.

    show_label:
        Whether to show the label.

    label_position:
        Position of the label relative to the object.

    fill_color:
        Color of the object fill.

    fill_opacity:
        Opacity of the object fill.

    stroke_color:
        Color of the object border.

    stroke_width:
        Width of the object border.
    """

    def __init__(
        self,
        width: float = 2.0,
        height: float = 1.5,
        mass: float = 1.0,
        position: list[float] | None = None,
        velocity: list[float] | None = None,
        label: str | None = None,
        show_label: bool = True,
        label_position: str = UP,
        fill_color: str = BLUE_E,
        fill_opacity: float = 0.5,
        stroke_color: str = WHITE,
        stroke_width: float = 2,
        **kwargs,
    ) -> None:
        self._width = width
        self._height = height

        super().__init__(
            mass=mass,
            position=position,
            velocity=velocity,
            label=label,
            show_label=show_label,
            label_position=label_position,
            fill_color=fill_color,
            fill_opacity=fill_opacity,
            stroke_color=stroke_color,
            stroke_width=stroke_width,
            **kwargs,
        )

    def _create_geometry(self) -> Rectangle:
        return Rectangle(
            width=self._width,
            height=self._height,
            fill_color=self._fill_color,
            fill_opacity=self._fill_opacity,
            stroke_color=self._stroke_color,
            stroke_width=self._stroke_width,
        )


class PhysicalCircle(PhysicalObject):
    """
    A physical circle (disk in 2D).

    Parameters
    ----------
    radius:
        Radius of the circle.

    mass:
        Mass of the object.

    position:
        Initial position of the object.

    velocity:
        Initial velocity vector.

    label:
        Optional label to display.

    show_label:
        Whether to show the label.

    label_position:
        Position of the label relative to the object.

    fill_color:
        Color of the object fill.

    fill_opacity:
        Opacity of the object fill.

    stroke_color:
        Color of the object border.

    stroke_width:
        Width of the object border.
    """

    def __init__(
        self,
        radius: float = 1.0,
        mass: float = 1.0,
        position: list[float] | None = None,
        velocity: list[float] | None = None,
        label: str | None = None,
        show_label: bool = True,
        label_position: str = UP,
        fill_color: str = BLUE_E,
        fill_opacity: float = 0.5,
        stroke_color: str = WHITE,
        stroke_width: float = 2,
        **kwargs,
    ) -> None:
        self._radius = radius

        super().__init__(
            mass=mass,
            position=position,
            velocity=velocity,
            label=label,
            show_label=show_label,
            label_position=label_position,
            fill_color=fill_color,
            fill_opacity=fill_opacity,
            stroke_color=stroke_color,
            stroke_width=stroke_width,
            **kwargs,
        )

    def _create_geometry(self) -> Circle:
        return Circle(
            radius=self._radius,
            fill_color=self._fill_color,
            fill_opacity=self._fill_opacity,
            stroke_color=self._stroke_color,
            stroke_width=self._stroke_width,
        )
