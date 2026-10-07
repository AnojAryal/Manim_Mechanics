from __future__ import annotations

from typing import Iterable

from manim import *


class MechanicalAnimation:
    """
    Utilities for creating common mechanics animations.

    These methods return Manim Animation objects that can be passed
    directly to Scene.play().
    """

    @staticmethod
    def apply_force(
        force_vector: Mobject,
        target: Mobject | None = None,
        duration: float = 1.0,
        **kwargs,
    ) -> Animation:
        """
        Animate a force vector appearing on a mechanical system.

        Parameters
        ----------
        force_vector:
            Force vector to display.

        target:
            Optional object receiving the force. Currently used as
            semantic information and reserved for future interaction
            animations.

        duration:
            Animation duration in seconds.

        **kwargs:
            Additional arguments passed to Create.
        """
        return Create(
            force_vector,
            run_time=duration,
            **kwargs,
        )

    @staticmethod
    def move_object(
        obj: Mobject,
        end_position: list[float],
        duration: float = 1.0,
        **kwargs,
    ) -> Animation:
        """
        Move an object to a new position.
        """
        target = obj.copy()
        target.move_to(end_position)

        return Transform(
            obj,
            target,
            run_time=duration,
            **kwargs,
        )

    @staticmethod
    def rotate_object(
        obj: Mobject,
        angle: float,
        duration: float = 1.0,
        **kwargs,
    ) -> Animation:
        """
        Rotate an object by the specified angle in radians.
        """
        return Rotate(
            obj,
            angle=angle,
            run_time=duration,
            **kwargs,
        )

    @staticmethod
    def transform_beam(
        beam: Mobject,
        new_length: float,
        new_height: float,
        duration: float = 1.0,
        **kwargs,
    ) -> Animation:
        """
        Transform a beam to new dimensions.
        """
        target = beam.copy()

        target.stretch_to_fit_width(
            new_length,
            about_point=beam.get_center(),
        )

        target.stretch_to_fit_height(
            new_height,
            about_point=beam.get_center(),
        )

        return Transform(
            beam,
            target,
            run_time=duration,
            **kwargs,
        )

    @staticmethod
    def show_force_appearance(
        force_vector: Mobject,
        duration: float = 0.5,
        **kwargs,
    ) -> Animation:
        """
        Animate a force vector appearing.
        """
        return Create(
            force_vector,
            run_time=duration,
            **kwargs,
        )

    @staticmethod
    def animate_load_movement(
        load: Mobject,
        new_position: float,
        beam_length: float,
        beam_height: float,
        duration: float = 1.0,
        **kwargs,
    ) -> Animation:
        """
        Move a load to a new position along a beam.

        Parameters
        ----------
        load:
            Load object.

        new_position:
            Position along the beam measured from its left side.

        beam_length:
            Total beam length.

        beam_height:
            Beam height.

        duration:
            Animation duration in seconds.
        """
        new_x = new_position - beam_length / 2

        target = load.copy()
        target.move_to(
            [
                new_x,
                beam_height / 2,
                0,
            ]
        )

        return Transform(
            load,
            target,
            run_time=duration,
            **kwargs,
        )

    @staticmethod
    def create_sequence(
        *animations: Animation,
        lag_ratio: float = 0.1,
        **kwargs,
    ) -> Animation:
        """
        Play multiple animations sequentially with optional overlap.

        A lag_ratio of 0 means all animations start together.
        A lag_ratio of 1 means each animation starts after the
        previous animation.
        """
        return AnimationGroup(
            *animations,
            lag_ratio=lag_ratio,
            **kwargs,
        )

    @staticmethod
    def create_parallel(
        *animations: Animation,
        **kwargs,
    ) -> Animation:
        """
        Play multiple animations simultaneously.
        """
        return AnimationGroup(
            *animations,
            lag_ratio=0,
            **kwargs,
        )

    @staticmethod
    def create_all(
        *objects: Mobject,
        lag_ratio: float = 0.2,
        **kwargs,
    ) -> Animation:
        """
        Create multiple objects with a controlled stagger.
        """
        animations = [
            Create(obj)
            for obj in objects
        ]

        return AnimationGroup(
            *animations,
            lag_ratio=lag_ratio,
            **kwargs,
        )


class ForceAnimation(VGroup):
    """
    Higher-level animated representation of a mechanical force.
    """

    def __init__(
        self,
        magnitude: float = 1.0,
        direction: str | float = "down",
        start_point: list[float] | None = None,
        label: str | None = None,
        color=WHITE,
        scale: float = 0.5,
        **kwargs,
    ) -> None:

        from .forces import ForceVector

        self.force_vector = ForceVector(
            magnitude=magnitude,
            direction=direction,
            start_point=start_point,
            label=label,
            show_label=True,
            color=color,
            scale=scale,
        )

        super().__init__(
            self.force_vector,
            **kwargs,
        )

    def animate_application(
        self,
        duration: float = 1.0,
    ) -> Animation:
        """
        Animate the force appearing.
        """
        return MechanicalAnimation.show_force_appearance(
            self.force_vector,
            duration=duration,
        )

    def animate_magnitude_change(
        self,
        new_magnitude: float,
        duration: float = 1.0,
    ) -> Animation:
        """
        Animate a change in force magnitude.
        """
        from .forces import ForceVector

        new_vector = ForceVector(
            magnitude=new_magnitude,
            direction=self.force_vector.direction,
            start_point=self.force_vector.start_point,
            label=self.force_vector.label_text,
            show_label=self.force_vector.show_label,
            color=self.force_vector.color,
            scale=self.force_vector.scale,
        )

        return Transform(
            self.force_vector,
            new_vector,
            run_time=duration,
        )


class SystemAnimation:
    """
    Utilities for animating interactions between mechanical objects.
    """

    @staticmethod
    def animate_interaction(
        obj1: Mobject,
        obj2: Mobject,
        interaction_type: str = "contact",
        duration: float = 1.0,
        **kwargs,
    ) -> Animation:
        """
        Animate an interaction between two objects.

        Supported interaction types:

        - contact
        - collision
        - separation
        """

        if interaction_type == "contact":
            return AnimationGroup(
                obj1.animate.shift(RIGHT * 0.1),
                obj2.animate.shift(LEFT * 0.1),
                run_time=duration,
                **kwargs,
            )

        if interaction_type == "collision":
            return AnimationGroup(
                obj1.animate.shift(RIGHT * 0.2),
                obj2.animate.shift(LEFT * 0.2),
                run_time=duration,
                **kwargs,
            )

        if interaction_type == "separation":
            return AnimationGroup(
                obj1.animate.shift(LEFT * 0.5),
                obj2.animate.shift(RIGHT * 0.5),
                run_time=duration,
                **kwargs,
            )

        raise ValueError(
            f"Unknown interaction type: {interaction_type!r}. "
            "Expected 'contact', 'collision', or 'separation'."
        )

    @staticmethod
    def animate_system_creation(
        *objects: Mobject,
        lag_ratio: float = 0.2,
        **kwargs,
    ) -> Animation:
        """
        Animate creation of an entire mechanical system.
        """
        creates = [
            Create(obj)
            for obj in objects
        ]

        return AnimationGroup(
            *creates,
            lag_ratio=lag_ratio,
            **kwargs,
        )

    @staticmethod
    def create_sequence(
        *animations: Animation,
        lag_ratio: float = 0.1,
    ) -> Animation:
        """
        Create a sequence of animations with a lag between them.

        Parameters
        ----------
        *animations:
            The animations to sequence.

        lag_ratio:
            The lag ratio between animations.

        Returns
        -------
        AnimationGroup
            An animation group with the specified lag.
        """
        return AnimationGroup(*animations, lag_ratio=lag_ratio)

    @staticmethod
    def create_parallel(
        *animations: Animation,
    ) -> Animation:
        """
        Create parallel animations that run simultaneously.

        Parameters
        ----------
        *animations:
            The animations to run in parallel.

        Returns
        -------
        AnimationGroup
            An animation group with all animations running simultaneously.
        """
        return AnimationGroup(*animations, lag_ratio=0)


class ForceAnimation(VGroup):
    """
    An animated force that can be shown being applied over time.

    This is a higher-level conceptual object that represents a force
    that can be animated being applied to an object.

    Parameters
    ----------
    magnitude:
        Magnitude of the force.

    direction:
        Direction of the force.

    start_point:
        Starting point of the force.

    label:
        Optional label for the force.

    color:
        Color of the force.

    scale:
        Scaling factor for arrow length.
    """

    def __init__(
        self,
        magnitude: float = 1.0,
        direction: str | float = "down",
        start_point: list[float] | None = None,
        label: str | None = None,
        color: str = WHITE,
        scale: float = 0.5,
        **kwargs,
    ) -> None:
        from .forces import ForceVector

        self.force_vector = ForceVector(
            magnitude=magnitude,
            direction=direction,
            start_point=start_point,
            label=label,
            show_label=True,
            color=color,
            scale=scale,
        )

        super().__init__(self.force_vector, **kwargs)

    def animate_application(self, duration: float = 1.0) -> Animation:
        """
        Return an animation of this force being applied.

        Parameters
        ----------
        duration:
            Duration of the animation.

        Returns
        -------
        Animation
            An animation of the force being applied.
        """
        return MechanicalAnimation.show_force_appearance(self.force_vector, duration=duration)

    def animate_magnitude_change(
        self,
        new_magnitude: float,
        duration: float = 1.0,
    ) -> Animation:
        """
        Animate changing the magnitude of the force.

        Parameters
        ----------
        new_magnitude:
            New magnitude of the force.

        duration:
            Duration of the animation.

        Returns
        -------
        Animation
            An animation of the magnitude changing.
        """
        from .forces import ForceVector

        new_vector = ForceVector(
            magnitude=new_magnitude,
            direction=self.force_vector.direction,
            start_point=self.force_vector.start_point,
            label=self.force_vector.label_text,
            show_label=self.force_vector.show_label,
            color=self.force_vector.color,
            scale=self.force_vector.scale,
        )

        return Transform(self.force_vector, new_vector, run_time=duration)


class SystemAnimation:
    """
    Helper class for animating mechanical systems.

    This class provides methods for animating interactions between
    multiple objects in a mechanical system.
    """

    @staticmethod
    def animate_interaction(
        obj1: VGroup,
        obj2: VGroup,
        interaction_type: str = "contact",
        duration: float = 1.0,
        **kwargs,
    ) -> Animation:
        """
        Animate an interaction between two objects.

        Parameters
        ----------
        obj1:
            First object.

        obj2:
            Second object.

        interaction_type:
            Type of interaction ("contact", "collision", "separation").

        duration:
            Duration of the animation.

        **kwargs:
            Additional arguments.

        Returns
        -------
        Animation
            An animation of the interaction.
        """
        if interaction_type == "contact":
            return MechanicalAnimation.create_parallel(
                obj1.animate(run_time=duration, **kwargs),
                obj2.animate(run_time=duration, **kwargs),
            )
        elif interaction_type == "collision":
            return MechanicalAnimation.create_sequence(
                obj1.animate(run_time=duration / 2, **kwargs),
                obj2.animate(run_time=duration / 2, **kwargs),
            )
        else:
            return MechanicalAnimation.create_parallel(
                obj1.animate(run_time=duration, **kwargs),
                obj2.animate(run_time=duration, **kwargs),
            )

    @staticmethod
    def animate_system_creation(
        *objects: VGroup,
        lag_ratio: float = 0.2,
    ) -> Animation:
        """
        Animate the creation of a mechanical system.

        Parameters
        ----------
        *objects:
            Objects to create.

        lag_ratio:
            Lag between object creations.

        Returns
        -------
        Animation
            An animation of the system being created.
        """
        creates = [Create(obj) for obj in objects]
        return MechanicalAnimation.create_sequence(*creates, lag_ratio=lag_ratio)
