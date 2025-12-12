# Visual Design: Backtracking

## Environment Overview

The Backtracking world presents problem-solving as navigating a branching maze of choices. The environment emphasizes the exploration and pruning of the search space, with visual cues showing which paths lead to solutions and which are abandoned.

### Background and Atmosphere

The scene is set in a mysterious labyrinth with a dark purple-blue gradient background (#0d0221 to #1a0533). Glowing paths wind through the space. Fog effects add depth and mystery. The atmosphere conveys exploration and discovery.

### Lighting

Active exploration paths glow with cyan light. Backtracked paths dim to a faint gray. Invalid choices flash red before being abandoned. Solution paths glow with bright gold. The current position has a pulsing indicator.

### Camera Behavior

The camera can orbit 360 degrees around the search tree or maze, zoom to see individual decisions, and follow the exploration in real-time. For tree visualizations, the camera can show the tree from above or at an angle. Time-lapse mode shows the entire search at high speed.

### Interaction Ideas

Clicking a node shows the current state and choices available. Users can input custom problem instances. Speed controls adjust animation pace. Step-by-step mode allows manual advancement. Toggle between tree view and problem-specific view.

---

## Sub-Concept 1: N-Queens Problem

### 3D Metaphor

The N-Queens problem is visualized as placing glowing queen pieces on a 3D chessboard, with conflict detection shown as laser beams.

**Chessboard Setup**:
- N×N grid of tiles
- Alternating light and dark squares
- 3D queen pieces
- Row and column labels

**Placement Animation**:
- Queens placed row by row
- Each placement attempt shown
- Valid placements glow green
- Conflicts shown as red laser beams (row, column, diagonal)

**Backtracking**:
- When no valid position in a row, queen removed
- Previous row's queen repositioned
- Removed queens fade out
- New attempt begins

**Solution Display**:
- Complete valid configuration
- All queens glow gold
- No conflict beams visible
- Solution count displayed

### Visual Elements

- 3D chessboard
- Queen pieces with glow effects
- Conflict laser beams
- Row/column/diagonal highlighting
- Solution counter

---

## Sub-Concept 2: Subset Generation

### 3D Metaphor

Subset generation is visualized as a binary decision tree where each level represents including or excluding an element.

**Tree Structure**:
- Root at top
- Each level represents one element
- Left branch: include element
- Right branch: exclude element
- Leaf nodes: complete subsets

**Exploration Animation**:
- Start at root
- Traverse left (include) first
- Reach leaf, record subset
- Backtrack, traverse right (exclude)
- Continue until all leaves visited

**Subset Display**:
- Each leaf shows its subset
- Current path highlighted
- Completed subsets listed
- Element inclusion shown on edges

**Set Visualization**:
- Original set displayed
- Current subset being built
- Elements added/removed during traversal

### Visual Elements

- Binary decision tree
- Include/exclude edge labels
- Leaf node subset displays
- Current path highlighting
- Subset collection panel

---

## Sub-Concept 3: Permutation Generation

### 3D Metaphor

Permutation generation is visualized as a tree where each level fills one position with remaining elements.

**Tree Structure**:
- Root represents empty permutation
- Each level fills next position
- Branches for each remaining element
- Leaf nodes: complete permutations

**Exploration Animation**:
- At each node, show available elements
- Choose element, add to permutation
- Recurse to next level
- Backtrack: remove element, try next

**Permutation Building**:
- Current partial permutation displayed
- Available elements shown
- Used elements marked
- Complete permutations collected

**Swap Visualization**:
- For in-place algorithm
- Elements swap positions
- Swap animation
- Unswap during backtrack

### Visual Elements

- Multi-branch tree
- Position indicators
- Available element pool
- Permutation builder display
- Swap animations

---

## Sub-Concept 4: Maze Solving

### 3D Metaphor

Maze solving is visualized as navigating a 3D maze with glowing paths showing exploration and backtracking.

**Maze Structure**:
- 3D walls and corridors
- Start position (green)
- Goal position (gold)
- Walls as solid blocks

**Exploration Animation**:
- Current position as glowing sphere
- Path behind glows cyan
- Try each direction (up, right, down, left)
- Mark visited cells

**Dead End Handling**:
- Dead end detected
- Path dims
- Backtrack to last junction
- Try next direction

**Solution Path**:
- When goal reached, path glows gold
- Optimal path highlighted
- Dead ends shown as dim trails
- Solution length displayed

### Visual Elements

- 3D maze structure
- Explorer sphere
- Path trail effects
- Visited cell markers
- Direction indicators

---

## Sub-Concept 5: Sudoku Solver

### 3D Metaphor

Sudoku solving is visualized as filling a 3D grid with numbered cubes, with constraint checking shown as highlighting.

**Grid Setup**:
- 9×9 grid of cells
- 3×3 box boundaries
- Given numbers as solid cubes
- Empty cells as transparent

**Solving Animation**:
- Find empty cell
- Try digits 1-9
- Check row, column, box constraints
- Valid digit placed (green glow)
- Invalid digit rejected (red flash)

**Constraint Visualization**:
- When checking, highlight row
- Highlight column
- Highlight 3×3 box
- Conflicts shown as red connections

**Backtracking**:
- When no valid digit, remove last placed
- Return to previous cell
- Try next digit
- Continue until solved

### Visual Elements

- 3D Sudoku grid
- Numbered cubes
- Constraint highlighting
- Conflict indicators
- Progress counter

---

## Sub-Concept 6: Search Tree Visualization

### 3D Metaphor

A general visualization of the backtracking search tree showing the exploration pattern.

**Tree Structure**:
- Nodes represent states
- Edges represent choices
- Depth represents decision level
- Leaves are terminal states

**State Information**:
- Each node shows current state
- Edge labels show choice made
- Node color indicates status
- Pruned branches marked

**Exploration Pattern**:
- DFS traversal order
- Current node highlighted
- Stack of ancestors shown
- Backtrack path visible

**Statistics Display**:
- Nodes explored
- Nodes pruned
- Solutions found
- Current depth

### Visual Elements

- 3D tree structure
- State node displays
- Choice edge labels
- Exploration order numbers
- Statistics panel

---

## Color Palette

| Element | Color | Hex Code |
|---------|-------|----------|
| Background | Deep Purple | #0d0221 |
| Active Path | Cyan | #00ffff |
| Backtracked Path | Dim Gray | #3a3a3a |
| Invalid/Conflict | Red | #ff3333 |
| Valid Choice | Green | #33ff33 |
| Solution Path | Gold | #ffd700 |
| Current Position | Bright White | #ffffff |
| Include Branch | Blue | #3498db |
| Exclude Branch | Orange | #e67e22 |
| Pruned Branch | Dark Red | #8b0000 |
| Wall | Dark Gray | #2c2c2c |
| Goal | Bright Gold | #ffcc00 |

---

## Animation Timing

- Choice selection: 200ms
- Exploration step: 300ms
- Conflict detection: 400ms (flash)
- Backtrack step: 250ms
- Path dimming: 300ms
- Solution reveal: 800ms
- Queen placement: 400ms
- Maze movement: 200ms
- Tree node expansion: 300ms
- Pruning animation: 350ms
- Camera transitions: 500ms ease-in-out
