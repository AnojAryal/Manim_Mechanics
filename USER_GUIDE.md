# Manim Mechanics User Guide

A comprehensive guide for professors and students on using Manim Mechanics to create educational mechanics animations.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Beams and Structural Mechanics](#beams-and-structural-mechanics)
3. [Forces and Loads](#forces-and-loads)
4. [Physical Objects](#physical-objects)
5. [Basic Shapes](#basic-shapes)
6. [Measurements and Labels](#measurements-and-labels)
7. [Animations](#animations)
8. [Complete Examples](#complete-examples)

---

## Getting Started

### Prerequisites

1. Install Python 3.9 or higher
2. Install Manim: `pip install manim`
3. Install Manim Mechanics: `pip install manim-mechanics`

### Your First Animation

Create a file `my_first_beam.py`:

```python
from manim import *
from manim_mechanics import Mechanics, PointLoad, Support

class MyFirstBeam(Scene):
    def construct(self):
        # Create a simply supported beam with a point load
        beam = Mechanics(
            length=10,              # Beam length in meters
            height=0.5,             # Visual height
            supports=[
                Support(position=0, type="pinned"),      # Left support
                Support(position=10, type="roller"),     # Right support
            ],
            point_loads=[
                PointLoad(
                    position=5,       # Load at center
                    magnitude=20,    # 20 kN
                    direction="down",
                    label="20 kN",
                ),
            ],
        )

        self.play(Create(beam))
        self.wait()
```

Run it:

```bash
manim -pql my_first_beam.py MyFirstBeam
```

---

## Beams and Structural Mechanics

### Support Types

Manim Mechanics supports four types of supports:

- **pinned** - Triangle support (allows rotation, prevents translation)
- **roller** - Triangle with wheels (allows rotation and horizontal translation)
- **fixed** - Fixed support (prevents rotation and translation)
- **free** - No support (free end)

```python
from manim_mechanics import Mechanics, Support

# Cantilever beam (fixed at left, free at right)
cantilever = Mechanics(
    length=6,
    height=0.5,
    supports=[
        Support(position=0, type="fixed"),
        Support(position=6, type="free"),
    ],
)
```

### Load Types

#### Point Loads

Single force applied at a specific point:

```python
from manim_mechanics import PointLoad

point_load = PointLoad(
    position=3,           # Position along beam (meters)
    magnitude=15,         # Force magnitude (kN)
    direction="down",     # "up", "down", "left", or "right"
    label="15 kN",        # Optional label
    color="red",          # Optional color
)
```

#### Distributed Loads

Load distributed over a segment:

```python
from manim_mechanics import DistributedLoad

distributed_load = DistributedLoad(
    start_position=2,    # Start of distributed load
    end_position=6,       # End of distributed load
    magnitude=5,          # Load intensity (kN/m)
    direction="down",
    label="5 kN/m",
    color="blue",
)
```

#### Moment Loads

Rotational moment at a point:

```python
from manim_mechanics import MomentLoad

moment_load = MomentLoad(
    position=4,
    magnitude=25,         # Moment magnitude (kN·m)
    direction="clockwise",  # "clockwise" or "counterclockwise"
    label="25 kN·m",
    color="yellow",
)
```

### Showing Dimensions

Add dimension labels to your beam:

```python
beam = Mechanics(
    length=10,
    height=0.5,
    supports=[...],
    point_loads=[...],
    show_dimensions=True,  # Show length labels
    dimension_color="white",
)
```

### Complete Beam Example

```python
class ComplexBeam(Scene):
    def construct(self):
        beam = Mechanics(
            length=12,
            height=0.5,
            supports=[
                Support(position=0, type="pinned"),
                Support(position=8, type="roller"),
                Support(position=12, type="free"),
            ],
            point_loads=[
                PointLoad(position=3, magnitude=10, direction="down", label="10 kN"),
                PointLoad(position=9, magnitude=15, direction="down", label="15 kN"),
            ],
            distributed_loads=[
                DistributedLoad(
                    start_position=4,
                    end_position=7,
                    magnitude=5,
                    direction="down",
                    label="5 kN/m",
                ),
            ],
            moment_loads=[
                MomentLoad(
                    position=8,
                    magnitude=20,
                    direction="clockwise",
                    label="20 kN·m",
                ),
            ],
            show_dimensions=True,
        )

        self.play(Create(beam))
        self.wait()
```

---

## Forces and Loads

### Force Vectors

Create standalone force vectors:

```python
from manim_mechanics import ForceVector

force = ForceVector(
    magnitude=10,              # Determines arrow length
    direction="down",          # "up", "down", "left", "right", or angle in degrees
    start_point=[0, 2, 0],    # Starting position [x, y, z]
    label="10 N",
    color="red",
    scale=0.5,                 # Scaling factor for arrow length
)

self.play(Create(force))
```

### Force Systems

Multiple forces acting at a point with resultant calculation:

```python
from manim_mechanics import Force, ForceSystem

forces = [
    Force(magnitude=10, direction="up", label="10 N", color="red"),
    Force(magnitude=8, direction="right", label="8 N", color="blue"),
    Force(magnitude=6, direction="down", label="6 N", color="green"),
]

system = ForceSystem(
    forces=forces,
    origin=ORIGIN,
    show_resultant=True,      # Show the resultant force vector
    resultant_color="yellow",
)

self.play(Create(system))
```

### Animating Force Changes

```python
class ChangingForce(Scene):
    def construct(self):
        force = ForceVector(
            magnitude=10,
            direction="down",
            start_point=[0, 2, 0],
            label="10 N",
        )

        self.play(Create(force))
        self.wait()

        # Increase magnitude
        self.play(force.animate.set_magnitude(20))
        self.wait()

        # Change direction
        self.play(force.animate.set_direction("up"))
        self.wait()
```

---

## Physical Objects

### Physical Box

```python
from manim_mechanics import PhysicalBox

box = PhysicalBox(
    width=2,
    height=1.5,
    mass=5.0,              # Mass in kg
    position=[-2, 0, 0],  # Initial position
    velocity=[1, 0, 0],    # Initial velocity [vx, vy, vz]
    label="m = 5 kg",
    show_label=True,
    label_position=UP,
    fill_color="blue",
)

self.play(Create(box))
```

### Physical Circle

```python
from manim_mechanics import PhysicalCircle

circle = PhysicalCircle(
    radius=1,
    mass=3.0,
    position=[2, 0, 0],
    label="m = 3 kg",
    fill_color="red",
)

self.play(Create(circle))
```

### Animating Physical Objects

```python
class MovingObjects(Scene):
    def construct(self):
        box = PhysicalBox(
            width=2,
            height=1.5,
            mass=5.0,
            position=[-3, 0, 0],
            label="m = 5 kg",
        )

        self.play(Create(box))
        self.wait()

        # Move to new position
        self.play(box.animate.move_to([0, 1, 0]), run_time=2)
        self.wait()

        # Update mass label
        box.set_mass(10.0)
        self.play(box.animate.move_to([3, 0, 0]), run_time=2)
        self.wait()
```

---

## Basic Shapes

### Square

```python
from manim_mechanics import Square

square = Square(
    side_length=2,
    fill_color="blue",
    fill_opacity=0.5,
    stroke_color="white",
    stroke_width=2,
)

self.play(Create(square))
```

### Rectangle

```python
from manim_mechanics import RectangleShape

rectangle = RectangleShape(
    width=3,
    height=1.5,
    fill_color="green",
)

self.play(Create(rectangle))
```

### Circle

```python
from manim_mechanics import CircleShape

circle = CircleShape(
    radius=1,
    fill_color="red",
)

self.play(Create(circle))
```

### Triangle

```python
from manim_mechanics import TriangleShape

triangle = TriangleShape(
    side_length=2,
    fill_color="yellow",
)

self.play(Create(triangle))
```

---

## Measurements and Labels

### Dimension Lines

```python
from manim_mechanics import DimensionLine

# Horizontal dimension
dim_x = DimensionLine(
    start_point=[-2, 1, 0],
    end_point=[2, 1, 0],
    label="4 m",
    offset=0.3,
    color="white",
    show_arrows=True,
)

# Vertical dimension
dim_y = DimensionLine(
    start_point=[-2, -1, 0],
    end_point=[-2, 1, 0],
    label="2 m",
    offset=0.3,
)

self.play(Create(dim_x), Create(dim_y))
```

### Angle Arcs

```python
from manim_mechanics import AngleArc

angle = AngleArc(
    vertex=[0, 0, 0],
    point1=[1, 0, 0],
    point2=[0, 1, 0],
    label="90°",
    radius=0.5,
    color="white",
    angle_type="inner",  # "inner" or "outer"
)

self.play(Create(angle))
```

### Value Labels

```python
from manim_mechanics import ValueLabel

label = ValueLabel(
    value="F = 100 N",
    position=[2, 1, 0],
    color="white",
    background=True,              # Show background rectangle
    background_color="black",
    background_opacity=0.7,
)

self.play(Create(label))
```

---

## Animations

### MechanicalAnimation Helper

The `MechanicalAnimation` class provides static methods for common animations:

```python
from manim_mechanics import MechanicalAnimation

# Apply a force
self.play(MechanicalAnimation.apply_force(force_vector, duration=1))

# Move an object
self.play(MechanicalAnimation.move_object(obj, [0, 1, 0], duration=2))

# Rotate an object
self.play(MechanicalAnimation.rotate_object(obj, PI/4, duration=1))

# Transform beam dimensions
self.play(MechanicalAnimation.transform_beam(beam, new_length=12, new_height=0.8))
```

### Animation Sequences

Run animations in sequence:

```python
self.play(
    MechanicalAnimation.create_sequence(
        Create(beam),
        Create(force1),
        Create(force2),
        lag_ratio=0.2,  # Delay between animations
    )
)
```

### Parallel Animations

Run animations simultaneously:

```python
self.play(
    MechanicalAnimation.create_parallel(
        obj1.animate.move_to([1, 0, 0]),
        obj2.animate.move_to([-1, 0, 0]),
    )
)
```

### Moving Loads Along Beams

```python
class MovingLoad(Scene):
    def construct(self):
        beam = Mechanics(
            length=8,
            height=0.5,
            supports=[
                Support(position=0, type="pinned"),
                Support(position=8, type="roller"),
            ],
            point_loads=[
                PointLoad(position=2, magnitude=10, direction="down", label="10 kN"),
            ],
        )

        self.play(Create(beam))
        self.wait()

        # Animate load moving along the beam
        for new_pos in [3, 4, 5, 6]:
            self.play(
                beam.point_load_objects.animate.move_to(
                    [new_pos - 4, 0.75, 0]
                ),
                run_time=1,
            )
        self.wait()
```

---

## Complete Examples

### Example 1: Simply Supported Beam with Moving Load

```python
from manim import *
from manim_mechanics import Mechanics, PointLoad, Support

class SimplySupportedBeam(Scene):
    def construct(self):
        beam = Mechanics(
            length=10,
            height=0.5,
            supports=[
                Support(position=0, type="pinned"),
                Support(position=10, type="roller"),
            ],
            point_loads=[
                PointLoad(
                    position=2,
                    magnitude=15,
                    direction="down",
                    label="15 kN",
                ),
            ],
            show_dimensions=True,
        )

        self.play(Create(beam))
        self.wait(1)

        # Move load across the beam
        positions = [2, 4, 6, 8]
        for pos in positions:
            self.play(
                beam.point_load_objects.animate.move_to([pos - 5, 0.75, 0]),
                run_time=1.5,
            )
        self.wait(2)
```

### Example 2: Free Body Diagram

```python
from manim import *
from manim_mechanics import PhysicalBox, ForceVector, DimensionLine

class FreeBodyDiagram(Scene):
    def construct(self):
        # Create a physical object
        box = PhysicalBox(
            width=3,
            height=2,
            mass=10,
            position=ORIGIN,
            label="m = 10 kg",
        )

        # Create forces
        weight = ForceVector(
            magnitude=10,
            direction="down",
            start_point=[0, 1, 0],
            label="mg",
            color="red",
        )

        normal = ForceVector(
            magnitude=10,
            direction="up",
            start_point=[0, -1, 0],
            label="N",
            color="blue",
        )

        applied = ForceVector(
            magnitude=5,
            direction="right",
            start_point=[-1.5, 0, 0],
            label="F",
            color="green",
        )

        # Add dimensions
        width_dim = DimensionLine(
            start_point=[-1.5, 1.2, 0],
            end_point=[1.5, 1.2, 0],
            label="3 m",
        )

        self.play(Create(box))
        self.play(Create(weight), Create(normal), Create(applied))
        self.play(Create(width_dim))
        self.wait()
```

### Example 3: Force System with Resultant

```python
from manim import *
from manim_mechanics import Force, ForceSystem

class ForceResultant(Scene):
    def construct(self):
        forces = [
            Force(magnitude=8, direction="up", label="8 N", color="red"),
            Force(magnitude=6, direction="right", label="6 N", color="blue"),
            Force(magnitude=4, direction=45, label="4 N", color="green"),  # 45 degrees
        ]

        # Show individual forces
        self.play(Create(ForceSystem(forces, origin=ORIGIN)))
        self.wait()

        # Show with resultant
        system_with_resultant = ForceSystem(
            forces=forces,
            origin=ORIGIN,
            show_resultant=True,
            resultant_color="yellow",
        )

        self.play(Transform(
            ForceSystem(forces, origin=ORIGIN),
            system_with_resultant
        ))
        self.wait()
```

### Example 4: Cantilever Beam with Multiple Loads

```python
from manim import *
from manim_mechanics import Mechanics, PointLoad, DistributedLoad, MomentLoad, Support

class CantileverBeam(Scene):
    def construct(self):
        beam = Mechanics(
            length=6,
            height=0.5,
            supports=[
                Support(position=0, type="fixed"),
                Support(position=6, type="free"),
            ],
            point_loads=[
                PointLoad(position=2, magnitude=10, direction="down", label="10 kN"),
                PointLoad(position=4, magnitude=15, direction="down", label="15 kN"),
            ],
            distributed_loads=[
                DistributedLoad(
                    start_position=3,
                    end_position=5,
                    magnitude=5,
                    direction="down",
                    label="5 kN/m",
                ),
            ],
            moment_loads=[
                MomentLoad(
                    position=6,
                    magnitude=20,
                    direction="clockwise",
                    label="20 kN·m",
                ),
            ],
            show_dimensions=True,
        )

        self.play(Create(beam))
        self.wait()
```

---

## Tips for Educators

1. **Start Simple**: Begin with basic beams and point loads before introducing distributed loads and moments
2. **Use Colors**: Different colors for different force types help students distinguish them
3. **Show Dimensions**: Enable `show_dimensions=True` to help students understand scale
4. **Animate Progressively**: Create animations step-by-step to explain concepts
5. **Label Everything**: Clear labels are essential for educational content
6. **Combine Concepts**: Use beams, forces, and measurements together for complete diagrams

## Tips for Students

1. **Understand the Physics**: Know what you want to visualize before coding
2. **Use the Documentation**: Refer to this guide for parameter details
3. **Experiment**: Try different parameters to see their effects
4. **Build Gradually**: Start with simple examples and add complexity
5. **Test Frequently**: Run your animations often to catch issues early
6. **Learn Manim**: Understanding basic Manim helps with custom animations

## Common Issues

### Issue: Animation looks too fast/slow

**Solution**: Adjust the `run_time` parameter in animations:

```python
self.play(Create(beam), run_time=2)  # Slower
self.play(Create(beam), run_time=0.5)  # Faster
```

### Issue: Labels overlap

**Solution**: Adjust `label_position` or manually position labels:

```python
load = PointLoad(
    position=4,
    magnitude=10,
    direction="down",
    label="10 kN",
)
load.label_obj.next_to(load.arrow, LEFT, buff=0.5)
```

### Issue: Objects not positioned correctly

**Solution**: Use Manim's positioning methods:

```python
obj.move_to([x, y, z])
obj.shift(RIGHT * 2)
obj.next_to(other_obj, UP)
```

## Further Resources

- [Manim Documentation](https://docs.manim.community/)
- [Manim GitHub](https://github.com/ManimCommunity/manim)
- [Physics Animation Examples](https://github.com/3b1b/videos)

## Getting Help

If you encounter issues or have questions:
1. Check this guide for similar examples
2. Review the Manim documentation
3. Open an issue on the Manim Mechanics GitHub repository
