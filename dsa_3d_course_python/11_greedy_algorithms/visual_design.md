# Visual Design: Greedy Algorithms

## Environment Overview

The Greedy Algorithms world presents decision-making as selecting the "best" option at each moment. The environment emphasizes the local nature of greedy choices and how they combine to form global solutions.

### Background and Atmosphere

The scene is set in a futuristic decision chamber with a deep purple gradient background (#1a0a2e to #2d1b4e). Floating platforms hold the problem elements. Golden particles drift through the space, representing potential choices. The atmosphere conveys strategic selection.

### Lighting

Selected elements glow with golden light. Rejected or unavailable options dim to gray. The current "best" choice pulses brighter than alternatives. Completed solution elements have a stable green glow.

### Camera Behavior

The camera can orbit 360 degrees around the problem space, zoom to see individual decisions, and follow the greedy selection process. For tree-building algorithms, the camera can show the bottom-up construction. Timeline views support horizontal panning.

### Interaction Ideas

Clicking an element shows its value/weight. Users can input custom problem instances. Speed controls adjust animation pace. Comparison mode shows greedy vs optimal solutions side by side.

---

## Sub-Concept 1: Activity Selection

### 3D Metaphor

Activities are horizontal bars on a 3D timeline. The greedy algorithm selects non-overlapping activities by always choosing the one that ends earliest.

**Timeline Visualization**:
- Horizontal axis represents time
- Each activity is a colored bar from start to end time
- Bars arranged vertically to show all activities
- Time markers along the axis

**Selection Process**:
- Sort activities by end time (bars reorder)
- Scanner moves left to right
- First activity selected (glows green)
- Each subsequent activity checked for overlap
- Non-overlapping activities added to solution
- Overlapping activities fade to gray

**Solution Display**:
- Selected activities form a non-overlapping set
- Total count displayed
- Timeline shows efficient coverage

### Visual Elements

- Activity bars with start/end labels
- Time axis with markers
- Selection scanner
- Green glow for selected
- Gray fade for rejected
- Activity count display

---

## Sub-Concept 2: Coin Change (Greedy)

### 3D Metaphor

Coins float in a cloud, and the greedy algorithm repeatedly selects the largest coin that fits the remaining amount.

**Coin Cloud**:
- Coins of different sizes float in 3D space
- Size proportional to denomination
- Multiple copies of each denomination
- Coins gently bob and rotate

**Selection Animation**:
- Target amount displayed prominently
- Largest valid coin glows brighter
- Selected coin floats down to solution pile
- Remaining amount updates
- Process repeats until amount is zero

**Solution Pile**:
- Selected coins stack in a pile
- Total value shown
- Coin count displayed
- Comparison with optimal (if different)

### Visual Elements

- Floating coin cloud
- Denomination labels on coins
- Target amount display
- Selection glow effect
- Solution pile formation
- Remaining amount counter

---

## Sub-Concept 3: Huffman Coding

### 3D Metaphor

Characters are weighted spheres that combine bottom-up to form an optimal encoding tree.

**Initial State**:
- Characters as labeled spheres
- Sphere size proportional to frequency
- Spheres arranged on a platform
- Frequency values displayed

**Tree Building**:
- Two smallest spheres highlighted
- Spheres rise and merge into parent node
- Parent has combined weight
- Process repeats with new node set
- Tree grows upward

**Final Tree**:
- Complete Huffman tree structure
- Paths from root to leaves
- Left edges labeled '0', right edges labeled '1'
- Character encodings displayed at leaves

**Encoding Display**:
- Each character's binary code shown
- Code length varies by frequency
- Total encoding size calculated
- Comparison with fixed-length encoding

### Visual Elements

- Weighted character spheres
- Merge animation (rise and combine)
- Tree structure with labeled edges
- Binary path highlighting
- Encoding table display

---

## Sub-Concept 4: Interval Scheduling

### 3D Metaphor

Jobs are 3D blocks on a timeline, and the goal is to maximize the number of non-overlapping jobs or minimize machines needed.

**Job Blocks**:
- Each job is a 3D rectangular block
- Length represents duration
- Position on timeline shows start/end
- Color coding by job type or priority

**Scheduling Animation**:
- Jobs sorted by end time (or start time)
- Greedy selection of compatible jobs
- Selected jobs move to "scheduled" track
- Rejected jobs fade or move to waiting area

**Multi-Machine View**:
- Multiple parallel tracks (machines)
- Jobs assigned to minimize machines
- Each machine is a separate timeline
- Color coding by machine assignment

### Visual Elements

- 3D job blocks
- Timeline tracks
- Machine assignment visualization
- Compatibility checking animation
- Schedule optimization display

---

## Sub-Concept 5: Minimum Spanning Tree (Conceptual)

### 3D Metaphor

Cities are floating platforms connected by potential roads (edges). The greedy algorithm builds a tree connecting all cities with minimum total edge weight.

**Graph Setup**:
- Cities as glowing platforms in 3D space
- Potential edges as dim connecting lines
- Edge weights displayed on hover
- All cities initially disconnected

**Kruskal's Algorithm**:
- Edges sorted by weight (shown as list)
- Smallest edge highlighted
- If it doesn't create cycle, add to tree
- Edge glows and thickens when added
- Cycle detection shown visually

**Prim's Algorithm**:
- Start from one city (highlighted)
- Find minimum edge to unvisited city
- Add edge and city to tree
- Frontier expands outward
- Tree grows from starting point

**Final Tree**:
- MST edges glow brightly
- Unused edges fade away
- Total weight displayed
- Tree structure clearly visible

### Visual Elements

- City platforms
- Edge connections with weights
- Tree growth animation
- Cycle detection visualization
- Weight accumulator display

---

## Sub-Concept 6: Greedy vs Optimal Comparison

### 3D Metaphor

Side-by-side comparison showing when greedy works and when it fails.

**Split View**:
- Left panel: Greedy solution
- Right panel: Optimal solution (DP)
- Same problem instance in both

**Coin Change Example**:
- Denominations [1, 3, 4], amount = 6
- Greedy: [4, 1, 1] = 3 coins
- Optimal: [3, 3] = 2 coins
- Visual difference highlighted

**Success Case**:
- Standard denominations [25, 10, 5, 1]
- Greedy produces optimal solution
- Both panels show same result
- "Greedy = Optimal" indicator

### Visual Elements

- Split-screen layout
- Solution comparison
- Coin/step count display
- Success/failure indicators
- Problem property explanation

---

## Color Palette

| Element | Color | Hex Code |
|---------|-------|----------|
| Background | Deep Purple | #1a0a2e |
| Selected | Golden | #ffd700 |
| Best Choice | Bright Gold | #ffec8b |
| Rejected | Dim Gray | #4a4a4a |
| Completed | Success Green | #2ecc71 |
| Activity Bar | Teal | #1abc9c |
| Coin | Gold Gradient | #ffd700 to #b8860b |
| Huffman Node | Soft Blue | #74b9ff |
| Tree Edge | White | #ffffff |
| Timeline | Silver | #bdc3c7 |
| MST Edge | Electric Blue | #00d4ff |
| City Platform | Purple | #9b59b6 |

---

## Animation Timing

- Greedy choice highlight: 400ms
- Selection animation: 500ms
- Rejection fade: 300ms
- Coin float down: 600ms
- Huffman merge: 700ms
- Tree edge addition: 400ms
- Sort reordering: 500ms
- Scanner movement: 200ms per element
- Solution celebration: 800ms
- Camera transitions: 500ms ease-in-out
