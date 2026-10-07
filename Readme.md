# Manim Mechanics - Architecture & Implementation

## Concept Overview

Manim Mechanics is a high-level abstraction layer for Manim that simplifies the creation of educational mechanics and physics animations. The core concept is **declarative visualization** - users describe physical objects and their properties in domain-specific terms, and the package automatically handles the underlying Manim geometry, positioning, and visualization.

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

### Key Design Principles

1. **Declarative over Imperative** - Describe *what* you want, not *how* to draw it
2. **Domain-first API** - Use physics terminology (force, mass, beam, support)
3. **Automatic Layout** - Package handles positioning and grouping
4. **Manim Native** - Objects are real Manim Mobjects, not wrappers
5. **Educational Focus** - Simple API for students, powerful enough for professors

---

## How It's Used

### User Workflow

1. **Install the package**
   ```bash
   pip install manim-mechanics
   ```

2. **Import and create objects**
   ```python
   from manim_mechanics import Mechanics, PointLoad, Support

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

3. **Animate with standard Manim**
   ```python
   self.play(Create(beam))
   self.play(beam.animate.shift(RIGHT))
   ```

### User Mental Model

Users think in terms of:
- **Physical entities** - beams, loads, supports, forces
- **Properties** - magnitude, direction, position, mass
- **Animations** - create, move, transform

Users don't need to think about:
- **Coordinates** - x, y, z positions
- **Geometry** - Triangles, arrows, lines
- **Grouping** - VGroups, submobjects
- **Styling** - Colors, stroke widths, opacities

---

## How It Was Implemented

### Architecture Overview

```
manim_mechanics/
├── __init__.py              # Package exports
├── build.py                 # Example scene
└── objects/
    ├── __init__.py          # Module exports
    ├── mechanics.py         # Beam mechanics (beams, supports, loads)
    ├── shapes.py            # Basic shapes (square, circle, etc.)
    ├── physical_object.py   # Physical objects (mass, position, velocity)
    ├── forces.py            # Force visualization
    ├── measurements.py      # Dimensions, angles, labels
    └── animations.py       # Animation helpers
```

### Implementation Strategy

#### 1. Inheritance from Manim Mobjects

All visual objects inherit from Manim's `VGroup` or specific Mobjects:

```python
class Mechanics(VGroup):
    # Inherits from VGroup, so it's a real Manim object
    # Can be used with Create, Transform, .animate, etc.
```

**Why this approach:**
- Full Manim compatibility out of the box
- No need for wrapper adapters
- Users can mix Manim Mechanics objects with raw Manim objects

#### 2. Dataclasses for Configuration

Configuration objects use Python dataclasses:

```python
@dataclass
class PointLoad:
    position: float
    magnitude: float
    direction: Literal["up", "down", "left", "right"] = "down"
    label: str | None = None
    color: str = "white"
```

**Why this approach:**
- Clean, declarative configuration
- Type hints for IDE support
- Immutable configuration (optional with frozen=True)
- Easy to serialize/deserialize

#### 3. Separation of Concerns

Each module handles a specific domain:

- **mechanics.py** - Structural mechanics (beams, supports, loads)
- **shapes.py** - Geometric shapes
- **physical_object.py** - Physical entities with mass/position
- **forces.py** - Force vectors and systems
- **measurements.py** - Annotations and dimensions
- **animations.py** - Animation helpers

**Why this approach:**
- Easy to maintain and extend
- Clear module boundaries
- Can import only what you need

#### 4. Private Attributes to Avoid Conflicts

Attributes that conflict with Manim properties use underscore prefix:

```python
class BasicShape(VGroup):
    def __init__(self, fill_color: str = BLUE_E, **kwargs):
        self._fill_color = fill_color  # Private to avoid conflict with VGroup.color
        super().__init__(**kwargs)
```

**Why this approach:**
- Manim's VGroup has `color`, `width`, `height` properties with setters
- Direct assignment triggers Manim's property logic before initialization
- Private attributes store values for later use in geometry creation

#### 5. Coordinate Transformation

Physical coordinates map to visual coordinates:

```python
def _position_to_x(self, position: float) -> float:
    """Convert a physical beam position into a Manim x-coordinate."""
    return position - self.beam_length / 2
```

**Why this approach:**
- Users think in physical coordinates (0 to length)
- Manim uses center-origin coordinates (-length/2 to +length/2)
- Transformation hides this complexity from users

#### 6. Lazy Geometry Creation

Geometry is created in `__init__` after configuration:

```python
def __init__(self, length, height, **kwargs):
    self.beam_length = length
    self.beam_height = height
    super().__init__(**kwargs)
    self.geometry = self._create_geometry()  # Created after super().__init__
    self.add(self.geometry)
```

**Why this approach:**
- Configuration values are stored first
- Geometry uses stored values during creation
- Avoids conflicts with Manim's initialization

---

## How It Was Built

### Development Process

#### Phase 1: Package Setup

1. **Created pyproject.toml**
   - Set up package metadata
   - Specified dependencies (manim >= 0.18.0)
   - Configured build system (setuptools)
   - Added development dependencies (pytest, black, ruff, mypy)

2. **Created project structure**
   - `src/manim_mechanics/` for package code
   - `tests/` for future tests
   - Proper `__init__.py` files for imports

#### Phase 2: Core Mechanics Module

1. **Started with existing beam implementation**
   - Improved the `Mechanics` class
   - Added validation for positions and dimensions
   - Enhanced support types (pinned, roller, fixed, free)

2. **Expanded load types**
   - Point loads (single force at a point)
   - Distributed loads (force over a segment)
   - Moment loads (rotational moment)

3. **Added dimension display**
   - Optional dimension labels on beams
   - Configurable color and style

#### Phase 3: Basic Shapes Module

1. **Created base class `BasicShape`**
   - Common interface for all shapes
   - Shared styling parameters (color, opacity, stroke)

2. **Implemented specific shapes**
   - `Square` - Equal side lengths
   - `RectangleShape` - Custom width/height
   - `CircleShape` - Radius-based
   - `TriangleShape` - Equilateral triangle

3. **Key implementation detail**
   - Used private attributes (`_width`, `_height`) to avoid Manim property conflicts
   - Geometry created in `_create_geometry()` methods

#### Phase 4: Physical Objects Module

1. **Created `PhysicalObject` base class**
   - Mass, position, velocity properties
   - Optional label display
   - Configurable label position

2. **Implemented specific objects**
   - `PhysicalBox` - Rectangular physical object
   - `PhysicalCircle` - Circular physical object

3. **Added methods for property updates**
   - `set_mass()`, `set_position()`, `set_velocity()`
   - Allows dynamic updates during animations

#### Phase 5: Forces Module

1. **Created `Force` dataclass**
   - High-level force specification
   - Magnitude, direction, label, color

2. **Implemented `ForceVector`**
   - Visual representation with arrow
   - Automatic label positioning
   - Support for cardinal directions and angles

3. **Implemented `ForceSystem`**
   - Multiple forces at a point
   - Automatic resultant calculation
   - Optional resultant display

#### Phase 6: Measurements Module

1. **Created `DimensionLine`**
   - Lines with arrows and labels
   - Automatic offset from measured object
   - Optional arrow display

2. **Created `AngleArc`**
   - Arc visualization for angles
   - Automatic angle calculation
   - Inner/outer angle options

3. **Created `ValueLabel`**
   - Text labels with optional background
   - Configurable background color and opacity

#### Phase 7: Animations Module

1. **Created `MechanicalAnimation` helper class**
   - Static methods for common animations
   - `apply_force()`, `move_object()`, `rotate_object()`
   - `transform_beam()`, `show_force_appearance()`
   - `create_sequence()`, `create_parallel()`

2. **Created `ForceAnimation`**
   - Animated force application
   - Magnitude change animations

3. **Created `SystemAnimation`**
   - System-level animations
   - Object interactions
   - System creation

#### Phase 8: Integration and Testing

1. **Updated package exports**
   - `__init__.py` exports all public classes
   - Organized by module/category

2. **Created test scenes**
   - `build.py` with example beam
   - Tested each module independently
   - Verified Manim compatibility

3. **Fixed bugs**
   - Manim property conflicts (used private attributes)
   - Color string handling (lowercase strings)
   - Animation methods (used Transform instead of .animate.move_to)

#### Phase 9: Documentation

1. **Created README.md**
   - Quick start guide
   - Installation instructions
   - Basic example

2. **Created USER_GUIDE.md**
   - Comprehensive usage guide
   - Examples for each module
   - Tips for educators and students
   - Common issues and solutions

3. **Created API_REFERENCE.md**
   - Complete API documentation
   - All classes and methods
   - Parameter descriptions
   - Usage examples

---

## Technical Decisions

### Why Dataclasses Instead of Classes for Configuration?

**Decision:** Use `@dataclass` for `PointLoad`, `DistributedLoad`, `MomentLoad`, `Support`, `Force`

**Reasons:**
- Less boilerplate code
- Automatic `__init__`, `__repr__`, `__eq__`
- Type hints for IDE support
- Easy to extend with `@dataclass(frozen=True)` for immutability

### Why VGroup Instead of Direct Mobject?

**Decision:** Visual objects inherit from `VGroup`

**Reasons:**
- Can contain multiple submobjects (geometry + labels)
- Built-in grouping and positioning methods
- Standard Manim pattern for composite objects
- Supports `.animate` syntax

### Why Separate Animation Module?

**Decision:** Create `animations.py` with helper classes

**Reasons:**
- Common patterns extracted to reusable methods
- Users don't need to remember specific animation sequences
- Can be extended with more complex animations
- Keeps animation logic separate from object logic

### Why String Colors Instead of Constants?

**Decision:** Accept color strings like `"red"`, `"blue"`

**Reasons:**
- Simpler for beginners
- Works with Manim's color parsing
- Can still use Manim constants if desired
- More flexible than hardcoded constants

### Why Optional Dimensions on Beams?

**Decision:** `show_dimensions` parameter defaults to `False`

**Reasons:**
- Not all animations need dimensions
- Reduces visual clutter
- Users can enable when needed
- Configurable color for different themes

---

## Extensibility

### Adding New Support Types

To add a new support type (e.g., "spring"):

1. Update `Support` type hint:
   ```python
   type: Literal["pinned", "roller", "fixed", "free", "spring"]
   ```

2. Add creation method in `Mechanics`:
   ```python
   def _create_spring_support(self, x: float) -> VGroup:
       # Create spring visualization
       return VGroup(spring_coil, ground_line)
   ```

3. Add to `_create_supports()`:
   ```python
   elif support.type == "spring":
       support_group = self._create_spring_support(x)
   ```

### Adding New Shape Types

To add a new shape (e.g., "Pentagon"):

1. Add class to `shapes.py`:
   ```python
   class PentagonShape(BasicShape):
       def __init__(self, side_length: float = 2.0, **kwargs):
           self._side_length = side_length
           super().__init__(**kwargs)
           self.geometry = self._create_geometry()
           self.add(self.geometry)

       def _create_geometry(self) -> Polygon:
           # Create pentagon geometry
           return Polygon(...)
   ```

2. Export in `shapes/__init__.py`

3. Export in package `__init__.py`

### Adding New Animation Helpers

To add a new animation (e.g., "elastic deformation"):

1. Add static method to `MechanicalAnimation`:
   ```python
   @staticmethod
   def elastic_deformation(obj: Mobject, strain: float, duration: float = 1.0) -> Animation:
       # Create and return animation
       return ...
   ```

2. Document in USER_GUIDE.md and API_REFERENCE.md

---

## Performance Considerations

### Geometry Creation

- All geometry created during `__init__`, not lazily
- Trade-off: Faster at runtime, slower at instantiation
- Suitable for educational animations (small number of objects)

### Label Creation

- Labels created only if `label` is provided
- Optional `show_label` parameter
- Reduces overhead when labels aren't needed

### Animation Efficiency

- Uses Manim's built-in animations (Create, Transform, Rotate)
- No custom animation renderers
- Leverages Manim's optimizations

---

## Limitations and Future Work

### Current Limitations

1. **2D Only** - No 3D mechanics support
2. **Static Geometry** - Beams are rectangles, not arbitrary shapes
3. **Simple Constraints** - Limited support for complex constraints
4. **No Physics Engine** - Objects don't simulate physics, only visualize

### Potential Future Enhancements

1. **3D Support** - Extend to 3D beams and forces
2. **Truss Systems** - Support for truss structures
3. **Physics Simulation** - Integrate with physics engines
4. **Reactions Calculation** - Automatically calculate support reactions
5. **Shear/Moment Diagrams** - Automatically generate diagrams
6. **Animation Templates** - Pre-built animation sequences for common concepts

---

## Conclusion

Manim Mechanics successfully abstracts away the complexity of Manim for educational mechanics animations. By providing domain-specific objects that handle their own visualization, it allows educators and students to focus on physics concepts rather than animation implementation details.

The architecture is:
- **Modular** - Clear separation of concerns
- **Extensible** - Easy to add new features
- **Compatible** - Works seamlessly with Manim
- **Educational** - Simple API for beginners, powerful for experts

The implementation follows Python and Manim best practices while introducing a higher-level abstraction layer that makes mechanics animations accessible to a broader audience.
