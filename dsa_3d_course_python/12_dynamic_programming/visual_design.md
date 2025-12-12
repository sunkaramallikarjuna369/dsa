# Visual Design: Dynamic Programming

## Environment Overview

The Dynamic Programming world presents problem-solving as filling a grid of interconnected tiles. The environment emphasizes how solutions to subproblems combine to solve larger problems, with visual cues showing dependencies and optimal paths.

### Background and Atmosphere

The scene is set in a futuristic computation chamber with a deep blue gradient background (#0a1628 to #1a2744). The DP table floats as a grid of translucent tiles. Soft ambient lighting creates depth. The atmosphere conveys systematic problem-solving.

### Lighting

Computed tiles glow with warm light (gold/orange). Uncomputed tiles remain dim and translucent. The current tile being computed pulses. Dependency arrows glow when active. The optimal path has a distinct bright trail.

### Camera Behavior

The camera can orbit 360 degrees around the DP table, zoom to see individual cell computations, and follow the fill pattern. For 2D tables, the camera can tilt to show the grid from above or at an angle. Time-lapse mode shows the entire computation at high speed.

### Interaction Ideas

Clicking a tile shows its value and the subproblems it depends on. Users can input custom problem instances. Speed controls adjust animation pace. Toggle between memoization and tabulation views. Hover shows the recurrence relation.

---

## Sub-Concept 1: Fibonacci with Memoization

### 3D Metaphor

Fibonacci computation is visualized as a 1D row of tiles, with recursive calls shown as a tree that collapses when cached values are reused.

**Tile Row**:
- Horizontal row of tiles for F(0) to F(n)
- Each tile shows its Fibonacci value when computed
- Tiles light up in computation order

**Recursive Tree Overlay**:
- Tree structure shows recursive calls
- Branches to already-computed values short-circuit
- Tree collapses as memoization kicks in

**Cache Visualization**:
- Computed values stored in glowing cache
- Cache hits shown as instant lookups
- Comparison with naive recursion (exponential calls)

### Visual Elements

- 1D tile row
- Recursive call tree
- Cache storage visualization
- Computation order numbers
- Time savings indicator

---

## Sub-Concept 2: 0/1 Knapsack Problem

### 3D Metaphor

The knapsack problem is visualized as a 2D grid where rows represent items and columns represent capacities.

**Grid Setup**:
- Rows: items (0 to n)
- Columns: capacities (0 to W)
- Each cell: maximum value achievable

**Fill Pattern**:
- Fill row by row, left to right
- Each cell considers: include item or exclude
- Value = max(exclude, include if fits)

**Decision Arrows**:
- Horizontal arrow: exclude item (value from above)
- Diagonal arrow: include item (value from above-left + item value)
- Arrow color indicates which choice was made

**Item Visualization**:
- Items shown as 3D objects with weight/value labels
- Selected items highlighted when included
- Final selection shown at the end

### Visual Elements

- 2D grid of tiles
- Item representations
- Include/exclude arrows
- Capacity meter
- Value accumulator
- Final item selection display

---

## Sub-Concept 3: Longest Common Subsequence (LCS)

### 3D Metaphor

LCS is visualized as a 2D grid where rows and columns represent characters of the two strings.

**Grid Setup**:
- Rows: characters of string 1 (+ empty prefix)
- Columns: characters of string 2 (+ empty prefix)
- Each cell: LCS length for prefixes

**Fill Pattern**:
- Fill row by row
- If characters match: diagonal + 1
- If no match: max(left, above)

**Match Highlighting**:
- Matching characters create diagonal arrows
- Non-matches create horizontal/vertical arrows
- Diagonal path shows the LCS

**Backtracking**:
- After filling, trace back from bottom-right
- Follow arrows to reconstruct LCS
- LCS characters highlighted in both strings

### Visual Elements

- 2D character grid
- String labels on axes
- Diagonal/horizontal/vertical arrows
- Match indicators
- LCS path highlighting
- Reconstructed subsequence display

---

## Sub-Concept 4: Coin Change (Minimum Coins)

### 3D Metaphor

Coin change is visualized as a 1D array where each position represents an amount, showing the minimum coins needed.

**Amount Array**:
- Horizontal row from 0 to target amount
- Each tile shows minimum coins for that amount
- Infinity symbol for impossible amounts

**Coin Consideration**:
- For each amount, try each coin denomination
- If coin fits: check amount - coin value
- Take minimum across all valid coins

**Coin Visualization**:
- Coins float above the array
- When considering a coin, it highlights
- Selected coins for each amount shown below

**Comparison with Greedy**:
- Side panel shows greedy result
- Highlight cases where DP beats greedy
- Example: [1, 3, 4] for amount 6

### Visual Elements

- 1D amount array
- Floating coin denominations
- Minimum coins counter per amount
- Coin selection visualization
- Greedy comparison panel

---

## Sub-Concept 5: Edit Distance

### 3D Metaphor

Edit distance is visualized as a 2D grid showing the minimum operations to transform one string into another.

**Grid Setup**:
- Rows: characters of source string (+ empty)
- Columns: characters of target string (+ empty)
- Each cell: minimum edit distance

**Operations**:
- Diagonal (match): no cost if characters equal
- Diagonal (replace): cost 1 if characters differ
- Horizontal (insert): cost 1
- Vertical (delete): cost 1

**Operation Arrows**:
- Green diagonal: match (free)
- Yellow diagonal: replace
- Blue horizontal: insert
- Red vertical: delete

**Transformation Path**:
- Backtrack to show sequence of operations
- Each operation animated on the strings
- Final transformation displayed

### Visual Elements

- 2D character grid
- Operation type arrows (colored)
- Cost accumulator
- String transformation animation
- Operation sequence display

---

## Sub-Concept 6: Longest Increasing Subsequence (LIS)

### 3D Metaphor

LIS is visualized as a 1D array with each position tracking the longest increasing subsequence ending at that index.

**Array Setup**:
- Original array as bar chart
- Below each bar: LIS length ending there
- Arrows show which previous element extends the LIS

**Computation**:
- For each element, check all previous elements
- If previous is smaller, consider extending its LIS
- Take maximum LIS length + 1

**Subsequence Highlighting**:
- Optimal LIS path highlighted
- Bars in LIS glow brighter
- Connecting arrows show the sequence

### Visual Elements

- Bar chart of array values
- LIS length tiles below bars
- Extension arrows
- Optimal path highlighting
- LIS reconstruction display

---

## Color Palette

| Element | Color | Hex Code |
|---------|-------|----------|
| Background | Deep Blue | #0a1628 |
| Uncomputed Tile | Dim Gray | #3d4f5f |
| Computing Tile | Pulse Yellow | #f1c40f |
| Computed Tile | Warm Orange | #e67e22 |
| Optimal Path | Bright Gold | #ffd700 |
| Match Arrow | Success Green | #2ecc71 |
| Insert Arrow | Sky Blue | #3498db |
| Delete Arrow | Coral Red | #e74c3c |
| Replace Arrow | Amber | #f39c12 |
| Cache Hit | Electric Cyan | #00d4ff |
| Dependency Arrow | Light Purple | #a29bfe |
| Grid Lines | Subtle Gray | #4a5568 |

---

## Animation Timing

- Tile computation: 300ms
- Arrow appearance: 200ms
- Cache lookup: 100ms (fast)
- Row/column fill: 150ms per cell
- Backtrack step: 400ms
- Path highlight: 500ms
- String transformation: 600ms per operation
- Memoization tree collapse: 300ms
- Final answer reveal: 800ms
- Camera transitions: 500ms ease-in-out
