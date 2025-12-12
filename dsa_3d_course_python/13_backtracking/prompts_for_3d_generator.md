# 3D Generator Prompts: Backtracking

These prompts are designed for use with 3D generation tools such as Three.js, WebGL, Blender scripting agents, or AI-powered 3D scene generators. Each prompt provides sufficient detail to create an educational, interactive 360-degree visualization.

---

## Prompt 1: N-Queens Problem Visualization

Generate a 360-degree, interactive 3D scene demonstrating the N-Queens problem for N=4. The background is a dark purple gradient (#0d0221 to #1a0533).

**Chessboard Setup**:
- 4×4 chessboard floating in space
- Alternating light (#f0d9b5) and dark (#b58863) squares
- 3D queen pieces with crown details
- Row labels (1-4) and column labels (a-d)

**Solving Animation**:

Step 1: Place Q1 at (0, 0)
- Queen appears on square a1
- Queen glows green (valid so far)

Step 2: Try Q2 at (1, 0)
- Attempt placement
- Red laser beam shows column conflict with Q1
- Placement rejected, try next column

Step 3: Try Q2 at (1, 1)
- Attempt placement
- Red diagonal beam shows conflict
- Rejected

Step 4: Place Q2 at (1, 2)
- Valid placement
- Queen glows green

Step 5: Try Q3 positions
- (2, 0): column conflict with Q1
- (2, 1): diagonal conflict with Q2
- (2, 2): column conflict with Q2
- (2, 3): diagonal conflict with Q2
- All rejected! Backtrack.

Step 6: Backtrack Q2
- Q2 removed from (1, 2)
- Q2 fades out
- Try Q2 at (1, 3)

(Continue until solution found)

**Solution Display**:
- Valid configuration: (0,1), (1,3), (2,0), (3,2)
- All queens glow gold
- No conflict beams
- "Solution 1 of 2" indicator

**Visual Elements**:
- 3D chessboard with depth
- Detailed queen pieces
- Conflict laser beams (red)
- Valid placement glow (green)
- Solution glow (gold)
- Backtrack animation (fade out)

---

## Prompt 2: Subset Generation Tree

Generate a 360-degree, interactive 3D scene demonstrating subset generation for set {1, 2, 3}. Show the binary decision tree.

**Tree Setup**:
- Root node at top center
- Three levels (one per element)
- Left branches: include element
- Right branches: exclude element
- 8 leaf nodes (2³ subsets)

**Tree Structure**:
```
                    {}
           /                 \
        {1}                   {}
       /    \               /    \
    {1,2}   {1}          {2}     {}
    /  \    /  \         /  \    /  \
{1,2,3}{1,2}{1,3}{1}  {2,3}{2}{3}  {}
```

**Exploration Animation**:

Step 1: Start at root {}
- Root node glows cyan
- "Current: {}" displayed

Step 2: Include 1, go left
- Edge to {1} lights up
- Node {1} glows
- "Include 1" label on edge

Step 3: Include 2, go left
- Edge to {1,2} lights up
- "Include 2" label

Step 4: Include 3, reach leaf
- Leaf {1,2,3} glows gold
- "Subset found: {1,2,3}"
- Add to collection

Step 5: Backtrack, exclude 3
- Path dims
- Go right to {1,2}
- "Exclude 3" label
- Leaf {1,2} glows gold

(Continue DFS traversal)

**Final Display**:
- All 8 subsets listed
- Tree fully explored
- Subsets: {}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}

**Visual Elements**:
- Binary tree structure
- Include/exclude edge labels
- Current path highlighting
- Leaf node subset displays
- Subset collection panel
- Exploration order numbers

---

## Prompt 3: Permutation Generation

Generate a 360-degree, interactive 3D scene demonstrating permutation generation for [1, 2, 3].

**Tree Setup**:
- Root represents choosing first position
- Second level: choosing second position
- Third level: choosing third position
- 6 leaf nodes (3! permutations)

**Permutation Building Display**:
- Three slots for the permutation: [ _ , _ , _ ]
- Available elements pool: {1, 2, 3}
- Current partial permutation shown

**Exploration Animation**:

Step 1: Choose 1 for position 0
- 1 moves from pool to slot 0
- [1, _, _]
- Available: {2, 3}

Step 2: Choose 2 for position 1
- 2 moves to slot 1
- [1, 2, _]
- Available: {3}

Step 3: Choose 3 for position 2
- 3 moves to slot 2
- [1, 2, 3] - Complete!
- Permutation glows gold
- Add to collection

Step 4: Backtrack
- 3 returns to pool
- 2 returns to pool
- [1, _, _]

Step 5: Choose 3 for position 1
- [1, 3, _]
- Available: {2}

Step 6: Choose 2 for position 2
- [1, 3, 2] - Complete!

(Continue until all 6 permutations found)

**Final Display**:
- All permutations: [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]
- Tree fully explored
- "6 permutations found"

**Visual Elements**:
- Permutation slots
- Element pool
- Tree structure
- Element movement animations
- Permutation collection

---

## Prompt 4: Maze Solving with Backtracking

Generate a 360-degree, interactive 3D scene demonstrating maze solving using backtracking.

**Maze Setup**:
- 5×5 grid maze
- Walls as 3D blocks
- Start position (0,0) - green glow
- Goal position (4,4) - gold glow
- Open paths as floor tiles

**Maze Layout**:
```
S . # . .
. # . # .
. . . . #
# . # . .
. . . . G
```
(S=start, G=goal, #=wall, .=path)

**Exploration Animation**:

Step 1: Start at (0,0)
- Explorer sphere at start
- Path begins glowing cyan

Step 2: Move right to (0,1)
- Sphere moves
- Trail extends
- Mark (0,0) as visited

Step 3: Try down from (0,1)
- Move to (1,1) - WALL!
- Red flash
- Can't go there

Step 4: Move down to (1,0)
- Valid move
- Trail extends

Step 5: Continue exploring...
- Try each direction
- Mark visited cells
- Backtrack from dead ends

Step 6: Dead end reached
- No valid moves
- Path dims
- Backtrack to last junction

Step 7: Find solution path
- Reach (4,4)
- Entire solution path glows gold
- "Path found! Length: X"

**Visual Elements**:
- 3D maze walls
- Explorer sphere
- Cyan exploration trail
- Gold solution path
- Dim backtracked paths
- Visited cell markers
- Direction arrows

---

## Prompt 5: Sudoku Solver Visualization

Generate a 360-degree, interactive 3D scene demonstrating Sudoku solving with backtracking.

**Grid Setup**:
- 9×9 grid of cells
- 3×3 box boundaries (thicker lines)
- Given numbers as solid blue cubes
- Empty cells as transparent frames

**Initial Puzzle** (simplified 4×4 for visualization):
```
1 . | . 4
. . | 1 .
----+----
. 1 | . .
4 . | . 1
```

**Solving Animation**:

Step 1: Find first empty cell (0,1)
- Cell highlights
- "Trying cell (0,1)"

Step 2: Try digit 2
- Check row 0: no 2 ✓
- Check column 1: no 2 ✓
- Check box: no 2 ✓
- Place 2, cube appears green

Step 3: Move to next empty (0,2)
- Try digit 3
- Valid, place it

Step 4: Continue filling...
- Each placement checked
- Valid placements glow green

Step 5: Conflict detected
- Try digit X at cell Y
- Row/column/box highlights red
- Digit rejected

Step 6: Backtrack
- Remove last placed digit
- Cube fades out
- Try next digit

Step 7: Solution found
- All cells filled
- Grid glows gold
- "Solved!"

**Visual Elements**:
- 3D Sudoku grid
- Number cubes
- Constraint highlighting (row, column, box)
- Conflict indicators
- Backtrack animations
- Progress indicator

---

## Prompt 6: Combination Sum Visualization

Generate a 360-degree, interactive 3D scene demonstrating finding combinations that sum to a target.

**Problem Setup**:
- Candidates: [2, 3, 6, 7]
- Target: 7
- Find all combinations summing to 7

**Tree Visualization**:
- Root: sum = 0, remaining = 7
- Each branch: add a candidate
- Prune when sum > target
- Leaf when sum = target

**Exploration Animation**:

Step 1: Start with sum = 0
- Root node
- "Target: 7, Current: 0"

Step 2: Try adding 2
- sum = 2, remaining = 5
- Branch extends

Step 3: Try adding 2 again
- sum = 4, remaining = 3
- Continue

Step 4: Try adding 2 again
- sum = 6, remaining = 1
- Continue

Step 5: Try adding 2 again
- sum = 8 > 7
- PRUNE! Branch turns red
- Backtrack

Step 6: Try adding 3
- sum = 6 + 3 = 9 > 7
- Prune

Step 7: Find [2, 2, 3]
- sum = 2 + 2 + 3 = 7
- Solution! Glows gold

Step 8: Find [7]
- Direct path
- sum = 7
- Solution!

**Final Display**:
- Solutions: [[2,2,3], [7]]
- Pruned branches shown dimmed
- Solution paths highlighted

**Visual Elements**:
- Decision tree
- Sum accumulator
- Candidate selection
- Pruning visualization
- Solution collection

---

## Prompt 7: General Backtracking Pattern

Generate a 360-degree, interactive 3D scene demonstrating the general "choose-explore-unchoose" pattern.

**Concept Visualization**:
- Three-phase cycle shown as rotating mechanism
- CHOOSE: Select an option (gear turns)
- EXPLORE: Recurse deeper (path extends)
- UNCHOOSE: Undo selection (gear reverses)

**State Display**:
- Current state box
- Available choices list
- Decision stack
- Exploration depth meter

**Animation Sequence**:

Phase 1: CHOOSE
- Options displayed
- One option highlighted
- "Choosing option X"
- Option added to stack

Phase 2: EXPLORE
- Recurse indicator
- Depth increases
- New state displayed
- "Exploring with X"

Phase 3: Base Case or Backtrack
- If solution: celebrate
- If dead end: UNCHOOSE
- Option removed from stack
- "Backtracking, unchoose X"

Phase 4: Try Next
- Next option highlighted
- Cycle repeats

**Code Synchronization**:
- Python code panel
- Current line highlighted
- Variable values shown
- Call stack visualization

**Visual Elements**:
- Three-phase mechanism
- State display
- Choice stack
- Depth meter
- Code panel
- Call stack

---

## General Requirements for All Prompts

- All scenes must support 360-degree camera orbit and zoom functionality
- Include educational labels with readable fonts (minimum 14pt equivalent)
- Use consistent color coding across all scenes as defined in the color palette
- Ensure interactive elements have clear hover states and click feedback
- Animations should be smooth (60fps target) with adjustable speed controls
- Include accessibility features: high contrast mode, colorblind-friendly palette
- All text labels should remain readable from any camera angle
- Export scenes in web-compatible formats (glTF, WebGL-ready)
- Include Python code snippets that highlight during relevant animation steps
- Provide step-by-step controls for educational walkthrough
- Show the "choose-explore-unchoose" pattern clearly in all visualizations
- Display statistics: nodes explored, pruned, solutions found
