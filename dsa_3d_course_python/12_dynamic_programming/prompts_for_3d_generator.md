# 3D Generator Prompts: Dynamic Programming

These prompts are designed for use with 3D generation tools such as Three.js, WebGL, Blender scripting agents, or AI-powered 3D scene generators. Each prompt provides sufficient detail to create an educational, interactive 360-degree visualization.

---

## Prompt 1: Fibonacci with Memoization vs Naive Recursion

Generate a 360-degree, interactive 3D scene comparing naive recursive Fibonacci with memoized Fibonacci. The background is a deep blue gradient (#0a1628 to #1a2744).

**Split View Setup**:
- Left panel: Naive recursion
- Right panel: Memoization
- Computing F(6) in both

**Naive Recursion (Left)**:
- Full binary tree of recursive calls
- F(6) at root
- F(5) and F(4) as children
- Continue expanding to F(0) and F(1) leaves
- Total nodes: 25 (exponential)
- Nodes light up as computed
- Many duplicate computations highlighted

**Memoization (Right)**:
- Same tree structure initially
- As values are computed, they're cached
- Duplicate calls short-circuit to cache
- Collapsed branches shown as dotted lines
- Total unique computations: 7 (linear)
- Cache panel shows stored values

**Animation Sequence**:
1. Both trees start expanding
2. Naive tree continues full expansion
3. Memoized tree collapses as cache fills
4. Side-by-side comparison of call counts
5. Final values displayed

**Visual Elements**:
- Binary tree nodes
- Cache storage visualization
- Call counter for each approach
- Duplicate computation highlighting
- Time complexity comparison: O(2^n) vs O(n)

---

## Prompt 2: 0/1 Knapsack DP Table

Generate a 360-degree, interactive 3D scene demonstrating the 0/1 knapsack problem with a DP table visualization.

**Problem Setup**:
- Items: [(weight=1, value=1), (weight=3, value=4), (weight=4, value=5), (weight=5, value=7)]
- Capacity: 7
- 5x8 grid (items 0-4 × capacities 0-7)

**Grid Visualization**:
- Floating 2D grid of translucent tiles
- Row 0: base case (no items, all zeros)
- Column 0: base case (zero capacity, all zeros)
- Items displayed as 3D objects beside their rows

**Fill Animation**:

Row 1 (item 0: w=1, v=1):
- For each capacity c from 1 to 7
- If c >= 1: max(above, above-left + 1)
- Tiles fill: [0, 1, 1, 1, 1, 1, 1, 1]

Row 2 (item 1: w=3, v=4):
- For c < 3: copy from above
- For c >= 3: max(above, dp[1][c-3] + 4)
- Tiles fill: [0, 1, 1, 4, 5, 5, 5, 5]

(Continue for all rows)

**Decision Arrows**:
- Vertical arrow: exclude item (value from above)
- Diagonal arrow: include item
- Arrow glows based on which choice was made

**Final Result**:
- Bottom-right cell: maximum value = 9
- Backtrack to show selected items
- Items 1 and 3 selected (w=3+5=8? No, w=3+4=7, v=4+5=9)

**Visual Elements**:
- 2D DP grid
- Item representations with weight/value
- Include/exclude arrows
- Backtracking path
- Selected items highlight

---

## Prompt 3: Longest Common Subsequence

Generate a 360-degree, interactive 3D scene demonstrating LCS computation for two strings.

**Problem Setup**:
- String 1: "ABCDGH"
- String 2: "AEDFHR"
- 7x7 grid (including empty prefix row/column)

**Grid Setup**:
- Rows labeled: "", A, B, C, D, G, H
- Columns labeled: "", A, E, D, F, H, R
- Each cell shows LCS length for prefixes

**Fill Animation**:

Base cases (row 0 and column 0): all zeros

Cell (1,1): A vs A
- Match! Diagonal + 1 = 0 + 1 = 1
- Green diagonal arrow

Cell (1,2): A vs E
- No match. max(left, above) = max(1, 0) = 1
- Horizontal arrow

Cell (2,1): B vs A
- No match. max(left, above) = max(0, 1) = 1
- Vertical arrow

(Continue filling entire grid)

**Match Highlighting**:
- When characters match, cell glows green
- Diagonal arrow appears
- Character pair highlighted in both strings

**Backtracking**:
- Start from bottom-right (value 3)
- Follow arrows back to find LCS
- LCS: "ADH"
- Path highlighted in gold

**Visual Elements**:
- Character grid with labels
- Diagonal/horizontal/vertical arrows
- Match indicators
- LCS path highlighting
- Reconstructed LCS display: "ADH"

---

## Prompt 4: Coin Change (Minimum Coins)

Generate a 360-degree, interactive 3D scene demonstrating the coin change problem with DP.

**Problem Setup**:
- Coins: [1, 3, 4]
- Target amount: 6
- 1D array from 0 to 6

**Array Visualization**:
- Horizontal row of 7 tiles (amounts 0-6)
- Coins floating above as 3D objects
- Each tile shows minimum coins needed

**DP Computation**:

Amount 0: 0 coins (base case)
Amount 1: min(dp[1-1]+1) = dp[0]+1 = 1 coin
Amount 2: min(dp[2-1]+1) = dp[1]+1 = 2 coins
Amount 3: min(dp[3-1]+1, dp[3-3]+1) = min(3, 1) = 1 coin
Amount 4: min(dp[4-1]+1, dp[4-3]+1, dp[4-4]+1) = min(2, 2, 1) = 1 coin
Amount 5: min(dp[5-1]+1, dp[5-3]+1, dp[5-4]+1) = min(2, 2, 2) = 2 coins
Amount 6: min(dp[6-1]+1, dp[6-3]+1, dp[6-4]+1) = min(3, 2, 3) = 2 coins

**Coin Selection Animation**:
- For each amount, show which coins are considered
- Highlight the optimal choice
- Show the coins used below each tile

**Greedy Comparison**:
- Side panel shows greedy approach
- Greedy for 6: [4, 1, 1] = 3 coins
- DP optimal: [3, 3] = 2 coins
- "DP beats greedy!" indicator

**Visual Elements**:
- 1D amount array
- Floating coins
- Minimum coins per amount
- Coin selection visualization
- Greedy vs DP comparison

---

## Prompt 5: Edit Distance (Levenshtein)

Generate a 360-degree, interactive 3D scene demonstrating edit distance computation.

**Problem Setup**:
- Source: "HORSE"
- Target: "ROS"
- 6x4 grid

**Grid Setup**:
- Rows: "", H, O, R, S, E
- Columns: "", R, O, S
- Each cell: minimum edits to transform prefix

**Base Cases**:
- Row 0: [0, 1, 2, 3] (insert each character)
- Column 0: [0, 1, 2, 3, 4, 5] (delete each character)

**Fill Animation**:

Cell (1,1): H → R
- H ≠ R, so consider:
  - Replace: dp[0][0] + 1 = 1
  - Insert: dp[1][0] + 1 = 2
  - Delete: dp[0][1] + 1 = 2
- Minimum: 1 (replace)
- Yellow diagonal arrow

Cell (2,2): HO → RO
- O = O, match!
- dp[1][1] + 0 = 1
- Green diagonal arrow

(Continue for all cells)

**Operation Arrows**:
- Green diagonal: match (cost 0)
- Yellow diagonal: replace (cost 1)
- Blue horizontal: insert (cost 1)
- Red vertical: delete (cost 1)

**Transformation Path**:
- Final cell: 3 edits
- Backtrack to find operations:
  1. Replace H with R
  2. Keep O
  3. Delete R
  4. Keep S
  5. Delete E
- Animate transformation: HORSE → RORSE → ROSE → ROS

**Visual Elements**:
- Character grid
- Operation arrows (colored by type)
- Edit distance values
- Transformation animation
- Operation sequence display

---

## Prompt 6: Longest Increasing Subsequence

Generate a 360-degree, interactive 3D scene demonstrating LIS computation.

**Problem Setup**:
- Array: [10, 9, 2, 5, 3, 7, 101, 18]
- Find longest increasing subsequence

**Visualization Setup**:
- Bar chart showing array values
- Below each bar: LIS length ending at that index
- Arrows showing which previous element extends LIS

**DP Computation**:

Index 0 (value 10): LIS = 1 (just itself)
Index 1 (value 9): No previous smaller, LIS = 1
Index 2 (value 2): No previous smaller, LIS = 1
Index 3 (value 5): 2 < 5, LIS = dp[2] + 1 = 2
Index 4 (value 3): 2 < 3, LIS = dp[2] + 1 = 2
Index 5 (value 7): max(dp[2], dp[3], dp[4]) + 1 = 3
Index 6 (value 101): max(all previous) + 1 = 4
Index 7 (value 18): max(dp[2], dp[3], dp[4], dp[5]) + 1 = 4

**Arrow Visualization**:
- For each element, arrows point to valid predecessors
- Optimal predecessor highlighted
- LIS path: 2 → 5 → 7 → 101 or 2 → 3 → 7 → 101

**Final Result**:
- Maximum LIS length: 4
- One valid LIS: [2, 5, 7, 101]
- Bars in LIS glow brighter

**Visual Elements**:
- Bar chart of values
- LIS length tiles
- Predecessor arrows
- Optimal path highlighting
- LIS reconstruction

---

## Prompt 7: DP State Transition Visualization

Generate a 360-degree, interactive 3D scene showing the general concept of DP state transitions.

**Concept Visualization**:
- 3D grid of states (nodes)
- Edges represent transitions
- Edge weights represent costs/values

**State Space**:
- Each node is a subproblem state
- Node value = optimal solution for that state
- Edges show dependencies

**Transition Animation**:
- Highlight current state being computed
- Show all incoming edges (dependencies)
- Compute value from dependencies
- Store result and move to next state

**Recurrence Relation Display**:
- Formula shown for current computation
- Variables highlighted in the grid
- Result calculation animated

**Examples Toggle**:
- Switch between different DP problems
- Show how state space changes
- Demonstrate 1D, 2D, and multi-dimensional DP

**Visual Elements**:
- State nodes in 3D space
- Transition edges with weights
- Recurrence formula display
- Computation order visualization
- Problem selector

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
- Show both memoization and tabulation approaches where applicable
- Display time and space complexity for each algorithm
