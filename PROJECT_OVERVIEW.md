# Manim Mechanics - Project Overview

## What is Manim Mechanics?

Manim Mechanics is a Python package that simplifies the creation of educational mechanics and physics animations using Manim. It provides a high-level, declarative API that allows educators and students to describe physical objects and their properties in domain-specific terms, while the package automatically handles the underlying Manim geometry, positioning, and visualization.

### The Problem It Solves

Creating mechanics animations with raw Manim requires:
- Deep knowledge of Manim's coordinate system and API
- Manual calculation of positions for every force, support, and label
- Repetitive code for common patterns (beams, forces, dimensions)
- Low-level manipulation of Mobjects for simple physical concepts

This creates a high barrier to entry for educators and students who want to focus on physics concepts rather than animation implementation details.

### The Solution

Manim Mechanics provides:
- **Domain-specific objects** - `Mechanics`, `PointLoad`, `Support`, `ForceVector`, etc.
- **Automatic positioning** - Physical coordinates map to visual coordinates
- **Built-in visualization** - Supports, arrows, labels are created automatically
- **Manim compatibility** - All objects work with standard Manim animations

---

## What Has Been Built

### Package Structure

```
manim_mechanics/
├── __init__.py                    # Main package exports
├── build.py                       # Example scenes
└── objects/
    ├── __init__.py                # Module exports
    ├── mechanics.py               # Beam mechanics (beams, supports, loads)
    ├── shapes.py                  # Basic shapes (square, circle, etc.)
    ├── physical_object.py         # Physical objects (mass, position, velocity)
    ├── forces.py                  # Force visualization
    ├── measurements.py            # Dimensions, angles, labels
    └── animations.py             # Animation helpers
```

### Core Modules

#### 1. Mechanics Module (`mechanics.py`)
**Purpose:** Structural mechanics visualization for beams and frames

**Components:**
- `Mechanics` class - Main beam object with supports and loads
- `PointLoad` - Single force at a specific point
- `DistributedLoad` - Force distributed over a segment
- `MomentLoad` - Rotational moment at a point
- `Support` - Support constraints (pinned, roller, fixed, free)

**Features:**
- Automatic support visualization (triangles, wheels, ground lines)
- Automatic load visualization (arrows, labels)
- Optional dimension display
- Coordinate transformation (physical to visual)

#### 2. Shapes Module (`shapes.py`)
**Purpose:** Basic geometric shapes with physical properties

**Components:**
- `Square` - Equal-sided square
- `RectangleShape` - Custom width/height rectangle
- `CircleShape` - Circle with radius
- `TriangleShape` - Equilateral triangle

**Features:**
- Configurable colors and styling
- Consistent interface via `BasicShape` base class

#### 3. Physical Objects Module (`physical_object.py`)
**Purpose:** Physical entities with mass, position, and velocity

**Components:**
- `PhysicalObject` - Base class for physical entities
- `PhysicalBox` - Rectangular physical object
- `PhysicalCircle` - Circular physical object

**Features:**
- Mass, position, velocity properties
- Optional labels
- Dynamic property updates (set_mass, set_position, set_velocity)

#### 4. Forces Module (`forces.py`)
**Purpose:** Force vector visualization

**Components:**
- `Force` - Dataclass for force specification
- `ForceVector` - Visual force arrow with label
- `ForceSystem` - Multiple forces with resultant calculation

**Features:**
- Support for cardinal directions and angles
- Automatic label positioning
- Resultant force calculation and display

#### 5. Measurements Module (`measurements.py`)
**Purpose:** Annotations and dimension visualization

**Components:**
- `DimensionLine` - Dimension lines with arrows and labels
- `AngleArc` - Angle visualization with arc
- `ValueLabel` - Text labels with optional background

**Features:**
- Automatic offset from measured objects
- Optional arrow display
- Configurable styling

#### 6. Animations Module (`animations.py`)
**Purpose:** Helper functions for common animations

**Components:**
- `MechanicalAnimation` - Static methods for common animations
- `ForceAnimation` - Animated force application
- `SystemAnimation` - System-level animations

**Features:**
- `apply_force()` - Show force application
- `move_object()` - Move objects to new positions
- `rotate_object()` - Rotate objects
- `transform_beam()` - Change beam dimensions
- `create_sequence()` - Sequential animations
- `create_parallel()` - Parallel animations

---

## Features

### 1. Declarative API
Describe *what* you want, not *how* to draw it:
```python
beam = Mechanics(
    length=10,
    height=0.5,
    supports=[Support(0, "pinned"), Support(10, "roller")],
    point_loads=[PointLoad(5, 20, "down", "20 kN")],
)
```

### 2. Automatic Positioning
No manual coordinate calculations - the package handles:
- Converting physical positions to Manim coordinates
- Positioning supports along beams
- Placing loads at correct locations
- Arranging labels automatically

### 3. Support Types
Four support types for different structural configurations:
- **Pinned** - Triangle support (allows rotation, prevents translation)
- **Roller** - Triangle with wheels (allows rotation and horizontal translation)
- **Fixed** - Fixed support (prevents rotation and translation)
- **Free** - No support (free end)

### 4. Load Types
Three types of loads for various mechanics problems:
- **Point Loads** - Single force at a point
- **Distributed Loads** - Force distributed over a segment
- **Moment Loads** - Rotational moment at a point

### 5. Force Visualization
Complete force system support:
- Individual force vectors with arrows and labels
- Multiple forces at a point
- Automatic resultant calculation
- Support for cardinal directions and custom angles

### 6. Physical Objects
Objects with physical properties:
- Mass, position, velocity
- Optional labels
- Dynamic property updates
- Multiple shapes (box, circle)

### 7. Measurements and Labels
Annotation tools:
- Dimension lines with arrows
- Angle arcs
- Value labels with optional backgrounds
- Automatic positioning

### 8. Animation Helpers
Pre-built animation patterns:
- Force application
- Object movement
- Rotation
- Beam transformation
- Sequential and parallel animations

### 9. Full Manim Compatibility
All objects are real Manim Mobjects:
- Work with `Create`, `Transform`, `.animate`, `FadeOut`
- Can be mixed with raw Manim objects
- No wrapper adapters needed

### 10. Color Customization
Flexible color system:
- String colors ("red", "blue", "green")
- Manim color constants (RED, BLUE, GREEN)
- Per-object color configuration

---

## How to Use

### Installation

```bash
pip install manim-mechanics
```

Or from source:
```bash
git clone https://github.com/yourusername/manim-mechanics.git
cd manim-mechanics
pip install -e .
```

### Requirements
- Python 3.9 or higher
- Manim 0.18.0 or higher

### Basic Usage

#### Step 1: Import the package
```python
from manim import *
from manim_mechanics import Mechanics, PointLoad, Support
```

#### Step 2: Create a Scene
```python
class MyScene(Scene):
    def construct(self):
        # Your animation code here
        pass
```

#### Step 3: Create objects
```python
beam = Mechanics(
    length=10,
    height=0.5,
    supports=[
        Support(position=0, type="pinned"),
        Support(position=10, type="roller"),
    ],
    point_loads=[
        PointLoad(
            position=5,
            magnitude=20,
            direction="down",
            label="20 kN",
        ),
    ],
)
```

#### Step 4: Animate
```python
self.play(Create(beam))
self.wait()
```

#### Step 5: Run the animation
```bash
manim -pql your_script.py MyScene
```

### Common Use Cases

#### 1. Simply Supported Beam
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
self.play(Create(beam))
```

#### 2. Cantilever Beam
```python
beam = Mechanics(
    length=6,
    height=0.5,
    supports=[
        Support(position=0, type="fixed"),
        Support(position=6, type="free"),
    ],
    point_loads=[
        PointLoad(position=6, magnitude=15, direction="down", label="15 kN"),
    ],
)
self.play(Create(beam))
```

#### 3. Complex Beam with Multiple Loads
```python
beam = Mechanics(
    length=12,
    height=0.5,
    supports=[
        Support(position=0, type="pinned"),
        Support(position=8, type="roller"),
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
```

#### 4. Free Body Diagram
```python
from manim_mechanics import PhysicalBox, ForceVector, DimensionLine

box = PhysicalBox(
    width=3,
    height=2,
    mass=10,
    position=ORIGIN,
    label="m = 10 kg",
)

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

self.play(Create(box), Create(weight), Create(normal))
```

#### 5. Force System with Resultant
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
    show_resultant=True,
    resultant_color="yellow",
)

self.play(Create(system))
```

#### 6. Moving Objects
```python
from manim_mechanics import PhysicalBox

box = PhysicalBox(
    width=2,
    height=1.5,
    mass=5.0,
    position=[-3, 0, 0],
    label="m = 5 kg",
)

self.play(Create(box))
self.play(box.animate.move_to([0, 1, 0]), run_time=2)
```

#### 7. Using Animation Helpers
```python
from manim_mechanics import MechanicalAnimation

self.play(
    MechanicalAnimation.move_object(obj, [0, 1, 0], duration=2),
    MechanicalAnimation.rotate_object(obj, PI/4, duration=1),
)
```

### Advanced Features

#### Custom Colors
```python
PointLoad(
    position=4,
    magnitude=10,
    direction="down",
    label="10 kN",
    color="red",  # or "blue", "green", etc.
)
```

#### Show Dimensions
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

#### Dynamic Property Updates
```python
box = PhysicalBox(mass=5.0, ...)
box.set_mass(10.0)  # Update mass
box.set_position([1, 2, 0])  # Update position
```

#### Custom Animation Sequences
```python
self.play(
    MechanicalAnimation.create_sequence(
        Create(beam),
        Create(force1),
        Create(force2),
        lag_ratio=0.2,
    )
)
```

---

## Benefits

### For Educators
1. **Quick Lesson Preparation** - Create animations in minutes, not hours
2. **Focus on Concepts** - Spend time on physics, not graphics
3. **Consistent Style** - Professional-looking animations automatically
4. **Easy Modifications** - Change parameters without rewriting code
5. **Teaching Tool** - Show code to students to demonstrate concepts

### For Students
1. **Low Barrier to Entry** - Simple API for beginners
2. **Learn Physics First** - Understand mechanics before learning graphics
3. **Experimentation** - Try different parameters easily
4. **Visualization** - See abstract concepts come to life
5. **Portfolio Building** - Create impressive animations for projects

### For Researchers
1. **Rapid Prototyping** - Test visualization ideas quickly
2. **Customizable** - Extend the package for specific needs
3. **Manim Compatible** - Mix with custom Manim code
4. **Well-Documented** - Comprehensive API reference
5. **Open Source** - Free to use and modify

---

## Documentation

The package includes comprehensive documentation:

1. **README.md** - Quick start guide and overview
2. **USER_GUIDE.md** - Detailed usage guide with examples
3. **API_REFERENCE.md** - Complete API documentation
4. **README_CONCEPT.md** - Architecture and implementation details

---

## Example Comparisons

### With Manim Mechanics (8 lines)
```python
beam = Mechanics(
    length=12,
    height=0.5,
    supports=[...],
    point_loads=[...],
    distributed_loads=[...],
    moment_loads=[...],
    show_dimensions=True,
)
self.play(Create(beam))
```

### With Raw Manim (120+ lines)
- Manual coordinate calculations
- Creating each support manually
- Positioning and rotating supports
- Creating each arrow for loads
- Looping for distributed loads
- Creating moment arcs
- Adding dimension lines
- Grouping everything manually

---

## Getting Started Checklist

- [ ] Install Python 3.9+
- [ ] Install Manim: `pip install manim`
- [ ] Install Manim Mechanics: `pip install manim-mechanics`
- [ ] Read the Quick Start guide in README.md
- [ ] Try the example in build.py
- [ ] Explore the USER_GUIDE.md for detailed examples
- [ ] Reference API_REFERENCE.md for available classes
- [ ] Create your first animation!

---

## Support and Resources

- **Documentation**: See README.md, USER_GUIDE.md, API_REFERENCE.md
- **Examples**: Check build.py for working examples
- **Manim Documentation**: https://docs.manim.community/
- **Issues**: Report bugs on GitHub repository

---

## License

MIT License - See LICENSE file for details
