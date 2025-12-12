# Visual Design: Searching Algorithms

## Environment Overview

The Searching Algorithms world presents arrays as illuminated corridors and trees as branching structures. The environment emphasizes the contrast between linear scanning and logarithmic divide-and-conquer approaches.

### Background and Atmosphere

The scene is set in a futuristic data center with dark metallic walls and glowing data streams. Arrays are displayed as corridors of illuminated tiles, while trees float as branching structures. The atmosphere conveys precision and efficiency.

### Lighting

Unsearched elements have dim ambient lighting. The current search position has a bright spotlight effect. Found elements glow green with success particles. Eliminated search space dims significantly to show it's no longer considered.

### Camera Behavior

The camera can orbit 360 degrees around the data structure, zoom to individual elements, and follow the search progress. For binary search, the camera can show the shrinking search space from above. For BST search, the camera follows the path down the tree.

### Interaction Ideas

Clicking an element shows its value and index. Users can input custom search targets. Speed controls adjust animation pace. Step-by-step mode allows manual progression through the algorithm.

---

## Sub-Concept 1: Linear Search

### 3D Metaphor

Linear search is visualized as a spotlight scanning through a corridor of elements from left to right, checking each one sequentially.

**Corridor Layout**:
- Array elements as floor tiles with glowing cubes
- Tiles numbered with indices (0, 1, 2, ...)
- Cubes display element values
- Corridor extends into the distance

**Spotlight Animation**:
- Bright spotlight starts at index 0
- Moves one tile at a time to the right
- Each tile briefly illuminated during check
- Comparison result shown (match/no match)

**Search States**:
- Unchecked: Dim ambient light
- Currently checking: Bright spotlight
- Checked (not found): Slightly dimmer than unchecked
- Found: Green glow with success particles

**Worst Case Visualization**:
- Target at end or not present
- Spotlight traverses entire corridor
- Counter shows number of comparisons
- O(n) complexity displayed

### Visual Elements

- Corridor of illuminated tiles
- Moving spotlight
- Comparison counter
- Found/not found indicators
- Complexity display

---

## Sub-Concept 2: Binary Search

### 3D Metaphor

Binary search is visualized as a corridor that shrinks by half with each comparison. The sorted nature of the array is emphasized by ascending values.

**Sorted Corridor**:
- Elements in ascending order (visible on cubes)
- Entire corridor initially lit
- Low, mid, high pointers shown as markers
- Values increase from left to right

**Divide and Conquer Animation**:
- Mid element highlighted with bright spotlight
- Comparison with target shown
- Half of corridor dims (eliminated from search)
- Remaining half becomes new search space
- Process repeats

**Pointer Visualization**:
- Low pointer: Blue marker at left boundary
- High pointer: Red marker at right boundary
- Mid pointer: Yellow marker at center
- Pointers move as search space shrinks

**Logarithmic Efficiency**:
- Search space size counter
- Halving animation clearly visible
- Comparison count vs array size
- O(log n) complexity displayed

### Visual Elements

- Sorted corridor with ascending values
- Low/mid/high pointer markers
- Dimming animation for eliminated half
- Search space size indicator
- Comparison counter

---

## Sub-Concept 3: Binary Search Variations

### 3D Metaphor

Variations of binary search (find first occurrence, find last occurrence, search insert position) are shown with modified highlighting to indicate boundaries.

**Find First Occurrence**:
- Multiple matching elements highlighted
- Search continues left after finding match
- First occurrence marked with special indicator
- Left boundary emphasized

**Find Last Occurrence**:
- Multiple matching elements highlighted
- Search continues right after finding match
- Last occurrence marked with special indicator
- Right boundary emphasized

**Search Insert Position**:
- Target not in array
- Search narrows to insertion point
- Gap between elements highlighted
- Insertion position marked

**Lower/Upper Bound**:
- Lower bound: First element >= target
- Upper bound: First element > target
- Boundary positions clearly marked
- Range of equal elements shown

### Visual Elements

- Duplicate element highlighting
- Boundary markers
- Insertion point indicator
- Range visualization
- Bound type labels

---

## Sub-Concept 4: BST Search

### 3D Metaphor

BST search is visualized as navigating through a tree structure, following the BST property to find the target.

**Tree Structure**:
- Nodes as glowing spheres with values
- Edges as connecting beams
- BST property: left < parent < right
- Color gradient showing value ordering

**Search Path Animation**:
- Start at root node
- Compare target with current node
- Go left if target < current, right if target > current
- Path glows as it's traversed

**Decision Visualization**:
- Current node highlighted
- Comparison result displayed
- Arrow indicates next direction
- Eliminated subtree dims

**Success/Failure States**:
- Found: Target node pulses green
- Not found: Reach null, path ends
- Path length displayed
- Comparison count shown

### Visual Elements

- Tree with BST ordering
- Glowing search path
- Direction arrows
- Comparison displays
- Subtree dimming

---

## Sub-Concept 5: Search in Rotated Array

### 3D Metaphor

A rotated sorted array is visualized as a corridor that has been "bent" at the rotation point, creating two sorted segments.

**Rotated Corridor**:
- Two sorted segments visible
- Rotation point marked
- Values jump from high to low at pivot
- Both segments still sorted individually

**Modified Binary Search**:
- Determine which half is sorted
- Check if target is in sorted half
- Eliminate appropriate half
- Handle rotation point

**Pivot Detection**:
- Pivot point highlighted
- Comparison with endpoints
- Sorted segment identification
- Search space selection

### Visual Elements

- Bent corridor visualization
- Pivot point marker
- Sorted segment indicators
- Modified search animation
- Segment comparison display

---

## Color Palette

| Element | Color | Hex Code |
|---------|-------|----------|
| Background | Dark Metallic | #1a1a2e |
| Unchecked Element | Dim Gray | #4a4a5a |
| Current Element | Bright Yellow | #f1c40f |
| Found Element | Success Green | #2ecc71 |
| Not Found | Dim Red | #c0392b |
| Eliminated Space | Very Dim | #2d2d3d |
| Low Pointer | Blue | #3498db |
| High Pointer | Red | #e74c3c |
| Mid Pointer | Yellow | #f39c12 |
| Search Path | Cyan | #00d4ff |
| BST Left | Cool Blue | #74b9ff |
| BST Right | Warm Orange | #fdcb6e |

---

## Animation Timing

- Linear search step: 300ms per element
- Binary search comparison: 400ms
- Half elimination: 500ms fade
- Pointer movement: 300ms
- BST node comparison: 400ms
- Path traversal: 350ms per edge
- Found celebration: 600ms
- Not found indication: 400ms
- Camera transitions: 500ms ease-in-out
