from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Optional

from manim import *


@dataclass
class Force:
    """
    A force with magnitude, direction, and optional label.

    This is a high-level representation of a force. The ForceVector class
    handles the visualization.

    Parameters
    ----------
    magnitude:
        Magnitude of the force.

    direction:
        Direction of the force ("up", "down", "left", "right", or angle in degrees).

    label:
        Optional label to display with the force.

    color:
        Color of the force arrow.
    """
    magnitude: float
    direction: str | float = "down"
    label: str | None = None
    color: str = "white"


class ForceVector(VGroup):
    """
    A visual representation of a force as an arrow with optional label.

    This is a higher-level conceptual object that represents a force vector.
    The user specifies the force properties, and the visualization is handled
    automatically.

    Parameters
    ----------
    magnitude:
        Magnitude of the force (determines arrow length).

    direction:
        Direction of the force ("up", "down", "left", "right", or angle in degrees).

    start_point:
        Starting point of the force vector [x, y, z].

    label:
        Optional label to display with the force.

    show_label:
        Whether to show the label.

    color:
        Color of the force arrow.

    scale:
        Scaling factor for arrow length (arrow_length = magnitude * scale).

    stroke_width:
        Width of the arrow line.
    """

    def __init__(
        self,
        magnitude: float = 1.0,
        direction: str | float = "down",
        start_point: list[float] | None = None,
        label: str | None = None,
        show_label: bool = True,
        color: str = WHITE,
        scale: float = 0.5,
        stroke_width: float = 4,
        **kwargs,
    ) -> None:
        self.magnitude = magnitude
        self.direction = direction
        self.start_point = start_point if start_point is not None else [0.0, 0.0, 0.0]
        self.label_text = label
        self.show_label = show_label
        self._color = color
        self.scale = scale
        self.stroke_width = stroke_width

        super().__init__(**kwargs)

        self.arrow = self._create_arrow()
        self.label_obj = self._create_label() if self.show_label and self.label_text else VGroup()

        self.add(self.arrow, self.label_obj)

    def _create_arrow(self) -> Arrow:
        """Create the force arrow based on magnitude and direction."""
        arrow_length = self.magnitude * self.scale
        end_point = self._calculate_end_point(arrow_length)

        return Arrow(
            start=self.start_point,
            end=end_point,
            buff=0,
            color=self._color,
            stroke_width=self.stroke_width,
        )

    def _calculate_end_point(self, length: float) -> list[float]:
        """Calculate the end point based on direction."""
        if isinstance(self.direction, str):
            if self.direction == "up":
                return [
                    self.start_point[0],
                    self.start_point[1] + length,
                    self.start_point[2],
                ]
            elif self.direction == "down":
                return [
                    self.start_point[0],
                    self.start_point[1] - length,
                    self.start_point[2],
                ]
            elif self.direction == "left":
                return [
                    self.start_point[0] - length,
                    self.start_point[1],
                    self.start_point[2],
                ]
            elif self.direction == "right":
                return [
                    self.start_point[0] + length,
                    self.start_point[1],
                    self.start_point[2],
                ]
            else:
                raise ValueError(f"Unknown direction: {self.direction}")
        else:
            angle_rad = self.direction * PI / 180
            return [
                self.start_point[0] + length * np.cos(angle_rad),
                self.start_point[1] + length * np.sin(angle_rad),
                self.start_point[2],
            ]

    def _create_label(self) -> MathTex:
        """Create a label for the force."""
        label = MathTex(self.label_text, color=self._color)
        label.next_to(self.arrow, self._get_label_direction(), buff=0.2)
        return label

    def _get_label_direction(self) -> str:
        """Determine the best direction for the label based on force direction."""
        if isinstance(self.direction, str):
            if self.direction == "up":
                return LEFT
            elif self.direction == "down":
                return RIGHT
            elif self.direction == "left":
                return UP
            elif self.direction == "right":
                return DOWN
        return UP

    def set_magnitude(self, magnitude: float) -> None:
        """Update the magnitude of the force."""
        self.magnitude = magnitude
        self.remove(self.arrow)
        self.arrow = self._create_arrow()
        self.add(self.arrow)
        if self.show_label and self.label_text:
            self.remove(self.label_obj)
            self.label_obj = self._create_label()
            self.add(self.label_obj)

    def set_direction(self, direction: str | float) -> None:
        """Update the direction of the force."""
        self.direction = direction
        self.remove(self.arrow)
        self.arrow = self._create_arrow()
        self.add(self.arrow)
        if self.show_label and self.label_text:
            self.remove(self.label_obj)
            self.label_obj = self._create_label()
            self.add(self.label_obj)

    def set_start_point(self, start_point: list[float]) -> None:
        """Update the start point of the force."""
        self.start_point = start_point
        self.remove(self.arrow)
        self.arrow = self._create_arrow()
        self.add(self.arrow)
        if self.show_label and self.label_text:
            self.remove(self.label_obj)
            self.label_obj = self._create_label()
            self.add(self.label_obj)


class ForceSystem(VGroup):
    """
    A system of multiple forces acting on an object or at a point.

    This is a higher-level conceptual object that represents a system of forces.
    The user specifies the forces, and the visualization is handled automatically.

    Parameters
    ----------
    forces:
        List of Force objects to visualize.

    origin:
        Origin point for all forces [x, y, z].

    show_resultant:
        Whether to show the resultant force vector.

    resultant_color:
        Color of the resultant force vector.

    scale:
        Scaling factor for arrow lengths.
    """

    def __init__(
        self,
        forces: list[Force],
        origin: list[float] | None = None,
        show_resultant: bool = False,
        resultant_color: str = YELLOW,
        scale: float = 0.5,
        **kwargs,
    ) -> None:
        self.forces = forces
        self.origin = origin if origin is not None else [0.0, 0.0, 0.0]
        self.show_resultant = show_resultant
        self._resultant_color = resultant_color
        self.scale = scale

        super().__init__(**kwargs)

        self.force_vectors = self._create_force_vectors()
        self.resultant_vector = self._create_resultant() if self.show_resultant else VGroup()

        self.add(self.force_vectors, self.resultant_vector)

    def _create_force_vectors(self) -> VGroup:
        """Create visual vectors for all forces."""
        vectors = VGroup()

        for force in self.forces:
            vector = ForceVector(
                magnitude=force.magnitude,
                direction=force.direction,
                start_point=self.origin,
                label=force.label,
                show_label=True,
                color=force.color,
                scale=self.scale,
            )
            vectors.add(vector)

        return vectors

    def _create_resultant(self) -> Arrow:
        """Create the resultant force vector."""
        rx, ry = 0.0, 0.0

        for force in self.forces:
            if isinstance(force.direction, str):
                if force.direction == "up":
                    ry += force.magnitude
                elif force.direction == "down":
                    ry -= force.magnitude
                elif force.direction == "left":
                    rx -= force.magnitude
                elif force.direction == "right":
                    rx += force.magnitude
            else:
                angle_rad = force.direction * PI / 180
                rx += force.magnitude * np.cos(angle_rad)
                ry += force.magnitude * np.sin(angle_rad)

        resultant_magnitude = np.sqrt(rx**2 + ry**2)
        if resultant_magnitude == 0:
            return Arrow(
                start=self.origin,
                end=self.origin,
                color=self.resultant_color,
            )

        end_point = [
            self.origin[0] + rx * self.scale,
            self.origin[1] + ry * self.scale,
            self.origin[2],
        ]

        return Arrow(
            start=self.origin,
            end=end_point,
            buff=0,
            color=self._resultant_color,
            stroke_width=5,
        )
