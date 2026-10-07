# Manim Mechanics API Reference

Complete API documentation for all Manim Mechanics classes and functions.

---

## Table of Contents

1. [Mechanics Module](#mechanics-module)
2. [Shapes Module](#shapes-module)
3. [Physical Objects Module](#physical-objects-module)
4. [Forces Module](#forces-module)
5. [Measurements Module](#measurements-module)
6. [Animations Module](#animations-module)

---

## Mechanics Module

### Classes

#### Mechanics

A conceptual mechanics beam with supports and loads.

```python
Mechanics(
    length: float,
    height: float,
    *,
    supports: list[Support] | None = None,
    point_loads: list[PointLoad] | None = None,
    distributed_loads: list[DistributedLoad] | None = None,
    moment_loads: list[MomentLoad] | None = None,
    show_dimensions: bool = False,
    dimension_color: str = WHITE,
    **kwargs,
)
```

**Parameters:**

- `length` (float): Physical length of the beam
- `height` (float): Visual height of the beam
- `supports` (list[Support] | None): Supports attached to the beam
- `point_loads` (list[PointLoad] | None): Point loads applied to the beam
- `distributed_loads` (list[DistributedLoad] | None): Distributed loads over beam segments
- `moment_loads` (list[MomentLoad] | None): Moment loads at specific positions
- `show_dimensions` (bool): Whether to show dimension labels
- `dimension_color` (str): Color for dimension labels

**Attributes:**

- `beam_length` (float): Length of the beam
- `beam_height` (float): Height of the beam
- `supports` (list[Support]): List of supports
- `point_loads` (list[PointLoad]): List of point loads
- `distributed_loads` (list[DistributedLoad]): List of distributed loads
- `moment_loads` (list[MomentLoad]): List of moment loads
- `geometry` (Rectangle): The beam geometry
- `support_objects` (VGroup): Visual support objects
- `point_load_objects` (VGroup): Visual point load objects
- `distributed_load_objects` (VGroup): Visual distributed load objects
- `moment_load_objects` (VGroup): Visual moment load objects
- `dimension_objects` (VGroup): Visual dimension objects

**Example:**

```python
beam = Mechanics(
    length=10,
    height=0.5,
    supports=[
        Support(position=0, type="pinned"),
        Support(position=10, type="roller"),
    ],
    point_loads=[
        PointLoad(position=5, magnitude=20, direction="down", label="20 kN"),
    ],
)
```

---

#### PointLoad

Dataclass representing a point load.

```python
@dataclass
class PointLoad:
    position: float
    magnitude: float
    direction: Literal["up", "down", "left", "right"] = "down"
    label: str | None = None
    color: str = "white"
```

**Parameters:**

- `position` (float): Position along the beam where the load is applied
- `magnitude` (float): Magnitude of the force
- `direction` (str): Direction of the force ("up", "down", "left", "right")
- `label` (str | None): Optional label to display
- `color` (str): Color of the force arrow

---

#### DistributedLoad

Dataclass representing a distributed load.

```python
@dataclass
class DistributedLoad:
    start_position: float
    end_position: float
    magnitude: float
    direction: Literal["up", "down"] = "down"
    label: str | None = None
    color: str = "white"
```

**Parameters:**

- `start_position` (float): Start position of the distributed load
- `end_position` (float): End position of the distributed load
- `magnitude` (float): Load intensity (force per unit length)
- `direction` (str): Direction of the load ("up" or "down")
- `label` (str | None): Optional label to display
- `color` (str): Color of the load arrows

---

#### MomentLoad

Dataclass representing a moment load.

```python
@dataclass
class MomentLoad:
    position: float
    magnitude: float
    direction: Literal["clockwise", "counterclockwise"] = "clockwise"
    label: str | None = None
    color: str = "white"
```

**Parameters:**

- `position` (float): Position where the moment is applied
- `magnitude` (float): Magnitude of the moment
- `direction` (str): Direction of rotation ("clockwise" or "counterclockwise")
- `label` (str | None): Optional label to display
- `color` (str): Color of the moment arc

---

#### Support

Dataclass representing a support constraint.

```python
@dataclass
class Support:
    position: float
    type: Literal["pinned", "roller", "fixed", "free"]
```

**Parameters:**

- `position` (float): Position of the support along the beam
- `type` (str): Type of support ("pinned", "roller", "fixed", "free")

**Support Types:**

- `pinned`: Triangle support (allows rotation, prevents translation)
- `roller`: Triangle with wheels (allows rotation and horizontal translation)
- `fixed`: Fixed support (prevents rotation and translation)
- `free`: No support (free end)

---

## Shapes Module

### Classes

#### Square

A square with physical dimensions.

```python
Square(
    side_length: float = 2.0,
    fill_color: str = BLUE_E,
    fill_opacity: float = 0.5,
    stroke_color: str = WHITE,
    stroke_width: float = 2,
    **kwargs,
)
```

**Parameters:**

- `side_length` (float): Length of each side
- `fill_color` (str): Color of the fill
- `fill_opacity` (float): Opacity of the fill (0-1)
- `stroke_color` (str): Color of the border
- `stroke_width` (float): Width of the border

---

#### RectangleShape

A rectangle with physical dimensions.

```python
RectangleShape(
    width: float = 3.0,
    height: float = 2.0,
    fill_color: str = BLUE_E,
    fill_opacity: float = 0.5,
    stroke_color: str = WHITE,
    stroke_width: float = 2,
    **kwargs,
)
```

**Parameters:**

- `width` (float): Width of the rectangle
- `height` (float): Height of the rectangle
- `fill_color` (str): Color of the fill
- `fill_opacity` (float): Opacity of the fill (0-1)
- `stroke_color` (str): Color of the border
- `stroke_width` (float): Width of the border

---

#### CircleShape

A circle with physical dimensions.

```python
CircleShape(
    radius: float = 1.0,
    fill_color: str = BLUE_E,
    fill_opacity: float = 0.5,
    stroke_color: str = WHITE,
    stroke_width: float = 2,
    **kwargs,
)
```

**Parameters:**

- `radius` (float): Radius of the circle
- `fill_color` (str): Color of the fill
- `fill_opacity` (float): Opacity of the fill (0-1)
- `stroke_color` (str): Color of the border
- `stroke_width` (float): Width of the border

---

#### TriangleShape

An equilateral triangle with physical dimensions.

```python
TriangleShape(
    side_length: float = 2.0,
    fill_color: str = BLUE_E,
    fill_opacity: float = 0.5,
    stroke_color: str = WHITE,
    stroke_width: float = 2,
    **kwargs,
)
```

**Parameters:**

- `side_length` (float): Length of each side
- `fill_color` (str): Color of the fill
- `fill_opacity` (float): Opacity of the fill (0-1)
- `stroke_color` (str): Color of the border
- `stroke_width` (float): Width of the border

---

## Physical Objects Module

### Classes

#### PhysicalObject

Base class for physical objects with mass, position, and dimensions.

```python
PhysicalObject(
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
)
```

**Parameters:**

- `mass` (float): Mass of the object
- `position` (list[float] | None): Initial position [x, y, z]
- `velocity` (list[float] | None): Initial velocity [vx, vy, vz]
- `label` (str | None): Optional label to display
- `show_label` (bool): Whether to show the label
- `label_position` (str): Position of label relative to object (UP, DOWN, LEFT, RIGHT)
- `fill_color` (str): Color of the fill
- `fill_opacity` (float): Opacity of the fill (0-1)
- `stroke_color` (str): Color of the border
- `stroke_width` (float): Width of the border

**Methods:**

- `set_mass(mass: float)`: Update the mass of the object
- `set_position(position: list[float])`: Update the position of the object
- `set_velocity(velocity: list[float])`: Update the velocity of the object

---

#### PhysicalBox

A physical box (rectangular prism in 2D).

```python
PhysicalBox(
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
)
```

**Additional Parameters:**

- `width` (float): Width of the box
- `height` (float): Height of the box

---

#### PhysicalCircle

A physical circle (disk in 2D).

```python
PhysicalCircle(
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
)
```

**Additional Parameters:**

- `radius` (float): Radius of the circle

---

## Forces Module

### Classes

#### Force

Dataclass representing a force.

```python
@dataclass
class Force:
    magnitude: float
    direction: str | float = "down"
    label: str | None = None
    color: str = "white"
```

**Parameters:**

- `magnitude` (float): Magnitude of the force
- `direction` (str | float): Direction ("up", "down", "left", "right", or angle in degrees)
- `label` (str | None): Optional label to display
- `color` (str): Color of the force arrow

---

#### ForceVector

Visual representation of a force as an arrow.

```python
ForceVector(
    magnitude: float = 1.0,
    direction: str | float = "down",
    start_point: list[float] | None = None,
    label: str | None = None,
    show_label: bool = True,
    color: str = WHITE,
    scale: float = 0.5,
    stroke_width: float = 4,
    **kwargs,
)
```

**Parameters:**

- `magnitude` (float): Magnitude of the force (determines arrow length)
- `direction` (str | float): Direction of the force
- `start_point` (list[float] | None): Starting point [x, y, z]
- `label` (str | None): Optional label to display
- `show_label` (bool): Whether to show the label
- `color` (str): Color of the force arrow
- `scale` (float): Scaling factor for arrow length (arrow_length = magnitude * scale)
- `stroke_width` (float): Width of the arrow line

**Methods:**

- `set_magnitude(magnitude: float)`: Update the magnitude of the force
- `set_direction(direction: str | float)`: Update the direction of the force
- `set_start_point(start_point: list[float])`: Update the start point of the force

---

#### ForceSystem

A system of multiple forces acting at a point.

```python
ForceSystem(
    forces: list[Force],
    origin: list[float] | None = None,
    show_resultant: bool = False,
    resultant_color: str = YELLOW,
    scale: float = 0.5,
    **kwargs,
)
```

**Parameters:**

- `forces` (list[Force]): List of Force objects to visualize
- `origin` (list[float] | None): Origin point for all forces [x, y, z]
- `show_resultant` (bool): Whether to show the resultant force vector
- `resultant_color` (str): Color of the resultant force vector
- `scale` (float): Scaling factor for arrow lengths

---

## Measurements Module

### Classes

#### DimensionLine

A dimension line with arrows and labels.

```python
DimensionLine(
    start_point: list[float],
    end_point: list[float],
    label: str | None = None,
    offset: float = 0.3,
    color: str = WHITE,
    show_arrows: bool = True,
    arrow_size: float = 0.15,
    **kwargs,
)
```

**Parameters:**

- `start_point` (list[float]): Starting point [x, y, z]
- `end_point` (list[float]): Ending point [x, y, z]
- `label` (str | None): Label to display for the dimension
- `offset` (float): Offset distance from the measured object
- `color` (str): Color of the dimension line and text
- `show_arrows` (bool): Whether to show arrows at the ends
- `arrow_size` (float): Size of the arrows

---

#### AngleArc

An angle arc with label.

```python
AngleArc(
    vertex: list[float],
    point1: list[float],
    point2: list[float],
    label: str | None = None,
    radius: float = 0.5,
    color: str = WHITE,
    angle_type: str = "inner",
    **kwargs,
)
```

**Parameters:**

- `vertex` (list[float]): Vertex point of the angle [x, y, z]
- `point1` (list[float]): First point defining the angle [x, y, z]
- `point2` (list[float]): Second point defining the angle [x, y, z]
- `label` (str | None): Label to display for the angle
- `radius` (float): Radius of the angle arc
- `color` (str): Color of the angle arc and text
- `angle_type` (str): Type of angle ("inner" or "outer")

---

#### ValueLabel

A value label with optional background.

```python
ValueLabel(
    value: str | float,
    position: list[float] | None = None,
    color: str = WHITE,
    background: bool = False,
    background_color: str = BLACK,
    background_opacity: float = 0.7,
    **kwargs,
)
```

**Parameters:**

- `value` (str | float): Value to display
- `position` (list[float] | None): Position of the label [x, y, z]
- `color` (str): Color of the text
- `background` (bool): Whether to show a background rectangle
- `background_color` (str): Color of the background
- `background_opacity` (float): Opacity of the background (0-1)

---

## Animations Module

### Classes

#### MechanicalAnimation

Helper class for creating common mechanical animations.

**Static Methods:**

##### apply_force

```python
MechanicalAnimation.apply_force(
    force_vector: Mobject,
    target: Mobject | None = None,
    duration: float = 1.0,
    **kwargs,
) -> Animation
```

Animate a force vector appearing.

**Parameters:**

- `force_vector` (Mobject): Force vector to display
- `target` (Mobject | None): Optional object receiving the force
- `duration` (float): Animation duration in seconds
- `**kwargs`: Additional arguments passed to Create

---

##### move_object

```python
MechanicalAnimation.move_object(
    obj: Mobject,
    end_position: list[float],
    duration: float = 1.0,
    **kwargs,
) -> Animation
```

Move an object to a new position.

**Parameters:**

- `obj` (Mobject): The object to move
- `end_position` (list[float]): The final position [x, y, z]
- `duration` (float): Animation duration in seconds
- `**kwargs`: Additional arguments passed to Transform

---

##### rotate_object

```python
MechanicalAnimation.rotate_object(
    obj: Mobject,
    angle: float,
    duration: float = 1.0,
    **kwargs,
) -> Animation
```

Rotate an object by the specified angle in radians.

**Parameters:**

- `obj` (Mobject): The object to rotate
- `angle` (float): Rotation angle in radians
- `duration` (float): Animation duration in seconds
- `**kwargs`: Additional arguments passed to Rotate

---

##### transform_beam

```python
MechanicalAnimation.transform_beam(
    beam: Mobject,
    new_length: float,
    new_height: float,
    duration: float = 1.0,
    **kwargs,
) -> Animation
```

Transform a beam to new dimensions.

**Parameters:**

- `beam` (Mobject): The beam object to transform
- `new_length` (float): New length of the beam
- `new_height` (float): New height of the beam
- `duration` (float): Animation duration in seconds
- `**kwargs`: Additional arguments passed to Transform

---

##### show_force_appearance

```python
MechanicalAnimation.show_force_appearance(
    force_vector: Mobject,
    duration: float = 0.5,
    **kwargs,
) -> Animation
```

Animate a force vector appearing with border drawing effect.

**Parameters:**

- `force_vector` (Mobject): The force vector to animate
- `duration` (float): Animation duration in seconds
- `**kwargs`: Additional arguments passed to DrawBorderThenFill

---

##### animate_load_movement

```python
MechanicalAnimation.animate_load_movement(
    load: Mobject,
    new_position: float,
    beam_length: float,
    beam_height: float,
    duration: float = 1.0,
    **kwargs,
) -> Animation
```

Animate a load moving along a beam.

**Parameters:**

- `load` (Mobject): The load object to move
- `new_position` (float): New position along the beam
- `beam_length` (float): Length of the beam
- `beam_height` (float): Height of the beam
- `duration` (float): Animation duration in seconds
- `**kwargs`: Additional arguments

---

##### create_sequence

```python
MechanicalAnimation.create_sequence(
    *animations: Animation,
    lag_ratio: float = 0.1,
) -> Animation
```

Create a sequence of animations with a lag between them.

**Parameters:**

- `*animations`: The animations to sequence
- `lag_ratio` (float): The lag ratio between animations

**Returns:** AnimationGroup with the specified lag

---

##### create_parallel

```python
MechanicalAnimation.create_parallel(
    *animations: Animation,
) -> Animation
```

Create parallel animations that run simultaneously.

**Parameters:**

- `*animations`: The animations to run in parallel

**Returns:** AnimationGroup with all animations running simultaneously

---

#### ForceAnimation

An animated force that can be shown being applied over time.

```python
ForceAnimation(
    magnitude: float = 1.0,
    direction: str | float = "down",
    start_point: list[float] | None = None,
    label: str | None = None,
    color: str = WHITE,
    scale: float = 0.5,
    **kwargs,
)
```

**Parameters:**

- `magnitude` (float): Magnitude of the force
- `direction` (str | float): Direction of the force
- `start_point` (list[float] | None): Starting point of the force
- `label` (str | None): Optional label for the force
- `color` (str): Color of the force
- `scale` (float): Scaling factor for arrow length

**Methods:**

- `animate_application(duration: float = 1.0) -> Animation`: Return an animation of this force being applied
- `animate_magnitude_change(new_magnitude: float, duration: float = 1.0) -> Animation`: Animate changing the magnitude of the force

---

#### SystemAnimation

Helper class for animating mechanical systems.

**Static Methods:**

##### animate_interaction

```python
SystemAnimation.animate_interaction(
    obj1: VGroup,
    obj2: VGroup,
    interaction_type: str = "contact",
    duration: float = 1.0,
    **kwargs,
) -> Animation
```

Animate an interaction between two objects.

**Parameters:**

- `obj1` (VGroup): First object
- `obj2` (VGroup): Second object
- `interaction_type` (str): Type of interaction ("contact", "collision", "separation")
- `duration` (float): Animation duration in seconds
- `**kwargs`: Additional arguments

**Returns:** Animation of the interaction

---

##### animate_system_creation

```python
SystemAnimation.animate_system_creation(
    *objects: VGroup,
    lag_ratio: float = 0.2,
) -> Animation
```

Animate the creation of a mechanical system.

**Parameters:**

- `*objects`: Objects to create
- `lag_ratio` (float): Lag between object creations

**Returns:** Animation of the system being created

---

## Color Constants

Manim Mechanics accepts color strings in lowercase:

- `"white"`, `"black"`, `"red"`, `"green"`, `"blue"`, `"yellow"`
- `"orange"`, `"purple"`, `"pink"`, `"cyan"`, `"magenta"`
- Manim color constants like `BLUE_E`, `RED`, `GREEN`, etc.

---

## Common Patterns

### Creating a Beam with Animation

```python
beam = Mechanics(length=10, height=0.5, supports=[...], point_loads=[...])
self.play(Create(beam), run_time=2)
```

### Moving Objects

```python
self.play(obj.animate.move_to([x, y, z]), run_time=1.5)
```

### Combining Animations

```python
self.play(
    Create(obj1),
    Create(obj2),
    Create(obj3),
    lag_ratio=0.2,
)
```

### Transforming Objects

```python
self.play(Transform(old_obj, new_obj), run_time=1)
```

---

## Notes

- All Manim Mechanics objects inherit from Manim's `VGroup` or `Mobject`
- They can be used with any standard Manim animation
- Positions are in Manim coordinate system (origin at center)
- Time units are in seconds unless otherwise specified
- Force magnitudes are arbitrary units for visualization
