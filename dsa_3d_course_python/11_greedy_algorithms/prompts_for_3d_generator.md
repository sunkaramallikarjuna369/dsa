# 3D Generator Prompts: Greedy Algorithms

These prompts are designed for use with 3D generation tools such as Three.js, WebGL, Blender scripting agents, or AI-powered 3D scene generators. Each prompt provides sufficient detail to create an educational, interactive 360-degree visualization.

---

## Prompt 1: Activity Selection Visualization

Generate a 360-degree, interactive 3D scene demonstrating the activity selection problem. The background is a deep purple gradient (#1a0a2e to #2d1b4e).

**Problem Setup**:
- 6 activities with start and end times:
  - A1: [1, 4], A2: [3, 5], A3: [0, 6], A4: [5, 7], A5: [3, 9], A6: [5, 9]
- Horizontal timeline from 0 to 10
- Each activity is a colored bar positioned on the timeline
- Bars arranged vertically to show all activities

**Greedy Algorithm Animation**:

Step 1: Sort by end time
- Activities reorder: A1[1,4], A2[3,5], A3[0,6], A4[5,7], A5[3,9], A6[5,9]
- Smooth reordering animation

Step 2: Select A1 (ends at 4)
- A1 glows green (selected)
- "Last end time: 4" indicator

Step 3: Check A2 (starts at 3)
- A2 highlighted for checking
- 3 < 4, overlaps with A1
- A2 fades to gray (rejected)

Step 4: Check A3 (starts at 0)
- 0 < 4, overlaps
- A3 fades to gray

Step 5: Select A4 (starts at 5)
- 5 >= 4, no overlap
- A4 glows green (selected)
- "Last end time: 7" indicator

Step 6: Check A5, A6
- Both start at 3 or 5, but end after 7
- Check if they overlap with A4
- A5 starts at 3 < 7, rejected
- A6 starts at 5 < 7, rejected

**Final Result**:
- Selected: A1, A4 (2 activities)
- Non-overlapping set highlighted
- "Maximum activities: 2" display

**Visual Elements**:
- Timeline with time markers
- Activity bars with labels
- Selection scanner moving left to right
- Green glow for selected activities
- Gray fade for rejected activities
- End time tracker

---

## Prompt 2: Coin Change Greedy Visualization

Generate a 360-degree, interactive 3D scene demonstrating greedy coin change. Show a floating coin cloud and the selection process.

**Problem Setup**:
- Denominations: [25, 10, 5, 1] (quarters, dimes, nickels, pennies)
- Target amount: 67 cents
- Coins float in a 3D cloud above a platform
- Coin sizes proportional to denomination

**Greedy Selection Animation**:

Step 1: Amount = 67
- Largest coin <= 67 is 25
- Quarter glows brighter
- Quarter floats down to solution pile
- Remaining: 67 - 25 = 42

Step 2: Amount = 42
- Largest coin <= 42 is 25
- Another quarter selected
- Remaining: 42 - 25 = 17

Step 3: Amount = 17
- Largest coin <= 17 is 10
- Dime selected
- Remaining: 17 - 10 = 7

Step 4: Amount = 7
- Largest coin <= 7 is 5
- Nickel selected
- Remaining: 7 - 5 = 2

Step 5: Amount = 2
- Largest coin <= 2 is 1
- Penny selected
- Remaining: 2 - 1 = 1

Step 6: Amount = 1
- Penny selected
- Remaining: 0

**Final Result**:
- Solution pile: 2 quarters, 1 dime, 1 nickel, 2 pennies
- Total coins: 6
- "Optimal for standard denominations" indicator

**Visual Elements**:
- Floating coin cloud with gentle motion
- Denomination labels on coins
- Target amount display (updating)
- Selection glow effect
- Solution pile formation
- Coin counter

---

## Prompt 3: Huffman Coding Tree Construction

Generate a 360-degree, interactive 3D scene demonstrating Huffman tree construction for data compression.

**Problem Setup**:
- Characters with frequencies: A:5, B:9, C:12, D:13, E:16, F:45
- Characters as weighted spheres on a platform
- Sphere size proportional to frequency
- Frequency labels displayed

**Tree Building Animation**:

Step 1: Initial state
- 6 spheres arranged on platform
- Sorted by frequency: A(5), B(9), C(12), D(13), E(16), F(45)

Step 2: Merge A(5) and B(9)
- Two smallest spheres highlighted
- Spheres rise and merge
- New node AB(14) created
- Tree level 1 formed

Step 3: Merge C(12) and D(13)
- Next two smallest: C(12), D(13)
- Merge into CD(25)

Step 4: Merge AB(14) and E(16)
- Smallest now: AB(14), E(16)
- Merge into ABE(30)

Step 5: Merge CD(25) and ABE(30)
- Merge into ABCDE(55)

Step 6: Merge ABCDE(55) and F(45)
- Final merge creates root(100)
- Complete tree formed

**Final Tree Display**:
- Tree structure clearly visible
- Left edges labeled '0', right edges labeled '1'
- Path from root to each leaf shown
- Encodings: F=0, C=100, D=101, A=1100, B=1101, E=111

**Visual Elements**:
- Weighted character spheres
- Merge animation (rise and combine)
- Tree structure with labeled edges
- Binary path highlighting
- Encoding table display
- Compression ratio calculation

---

## Prompt 4: Interval Scheduling Maximization

Generate a 360-degree, interactive 3D scene demonstrating interval scheduling to maximize the number of non-overlapping jobs.

**Problem Setup**:
- 7 jobs with intervals:
  - J1: [0, 3], J2: [1, 4], J3: [2, 5], J4: [4, 6], J5: [5, 8], J6: [6, 9], J7: [8, 10]
- Jobs as 3D blocks on a timeline
- Different colors for each job

**Greedy Scheduling Animation**:

Step 1: Sort by end time
- Jobs reorder by finish time
- J1[0,3], J2[1,4], J3[2,5], J4[4,6], J5[5,8], J6[6,9], J7[8,10]

Step 2: Select J1 (ends at 3)
- J1 moves to "scheduled" track
- Glows green
- End marker at 3

Step 3: Check J2 (starts at 1)
- 1 < 3, overlaps
- J2 fades to gray

Step 4: Check J3 (starts at 2)
- 2 < 3, overlaps
- J3 fades to gray

Step 5: Select J4 (starts at 4)
- 4 >= 3, compatible
- J4 moves to scheduled track
- End marker at 6

Step 6: Check J5 (starts at 5)
- 5 < 6, overlaps
- J5 fades to gray

Step 7: Select J6 (starts at 6)
- 6 >= 6, compatible
- J6 moves to scheduled track
- End marker at 9

Step 8: Check J7 (starts at 8)
- 8 < 9, overlaps
- J7 fades to gray

**Final Result**:
- Scheduled: J1, J4, J6 (3 jobs)
- Maximum non-overlapping set
- Timeline shows efficient coverage

---

## Prompt 5: Greedy Failure Case - Coin Change

Generate a 360-degree, interactive 3D scene demonstrating when greedy fails for coin change, with side-by-side comparison to optimal solution.

**Problem Setup**:
- Denominations: [1, 3, 4]
- Target amount: 6
- Split screen: Greedy (left) vs Optimal (right)

**Greedy Solution (Left Panel)**:

Step 1: Amount = 6
- Largest coin <= 6 is 4
- Select 4
- Remaining: 2

Step 2: Amount = 2
- Largest coin <= 2 is 1
- Select 1
- Remaining: 1

Step 3: Amount = 1
- Select 1
- Remaining: 0

Result: [4, 1, 1] = 3 coins

**Optimal Solution (Right Panel)**:

Step 1: Consider all possibilities
- DP table visualization
- Subproblems computed

Step 2: Optimal for 6
- 6 = 3 + 3
- Two coins of denomination 3

Result: [3, 3] = 2 coins

**Comparison Display**:
- Greedy: 3 coins (suboptimal)
- Optimal: 2 coins
- "Greedy fails for non-standard denominations"
- Explanation of why greedy choice property doesn't hold

**Visual Elements**:
- Split-screen layout
- Coin selection animations
- Solution piles for comparison
- Coin count display
- Failure/success indicators

---

## Prompt 6: Jump Game Greedy Visualization

Generate a 360-degree, interactive 3D scene demonstrating the jump game problem solved greedily.

**Problem Setup**:
- Array: [2, 3, 1, 1, 4]
- Platforms at each index
- Platform height indicates jump power
- Goal: Reach the last platform

**Greedy Algorithm Animation**:

Step 1: Start at index 0
- Platform 0 highlighted (jump power 2)
- Can reach indices 1 or 2
- Farthest reachable: 0 + 2 = 2

Step 2: Check index 1
- Jump power 3
- Can reach up to 1 + 3 = 4
- Update farthest: max(2, 4) = 4

Step 3: Check index 2
- Jump power 1
- Can reach up to 2 + 1 = 3
- Farthest still 4

Step 4: Farthest >= last index (4)
- Can reach the end!
- Success path highlighted

**Visual Elements**:
- Platforms with jump power indicators
- Reachable range visualization
- Farthest marker moving forward
- Success/failure indication
- Jump arc animations

---

## Prompt 7: Minimum Spanning Tree (Kruskal's Concept)

Generate a 360-degree, interactive 3D scene demonstrating Kruskal's algorithm for finding a minimum spanning tree.

**Graph Setup**:
- 5 cities as floating platforms: A, B, C, D, E
- Edges with weights:
  - A-B: 4, A-C: 2, B-C: 1, B-D: 5, C-D: 8, C-E: 10, D-E: 2
- All edges shown as dim connecting lines

**Kruskal's Algorithm Animation**:

Step 1: Sort edges by weight
- Edge list: B-C(1), A-C(2), D-E(2), A-B(4), B-D(5), C-D(8), C-E(10)

Step 2: Add B-C (weight 1)
- Smallest edge, no cycle
- Edge glows and thickens
- MST weight: 1

Step 3: Add A-C (weight 2)
- No cycle with existing edges
- Edge added to MST
- MST weight: 3

Step 4: Add D-E (weight 2)
- No cycle (D, E not yet connected)
- Edge added
- MST weight: 5

Step 5: Add A-B (weight 4)
- Would create cycle A-B-C-A
- Edge rejected (shown in red briefly)

Step 6: Add B-D (weight 5)
- Connects component {A,B,C} to {D,E}
- Edge added
- MST weight: 10

Step 7: MST Complete
- 4 edges connecting 5 vertices
- All cities connected
- Total weight: 10

**Visual Elements**:
- City platforms in 3D space
- Edge connections with weight labels
- Sorted edge list display
- Cycle detection visualization
- MST edges glowing brightly
- Weight accumulator

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
- Show when greedy produces optimal vs suboptimal solutions
