# 3D Generator Prompts: Advanced Data Structures

These prompts are designed for use with 3D generation tools such as Three.js, WebGL, Blender scripting agents, or AI-powered 3D scene generators. Each prompt provides sufficient detail to create an educational, interactive 360-degree visualization.

---

## Prompt 1: Trie Structure and Insert Operation

Generate a 360-degree, interactive 3D scene demonstrating a Trie structure with word insertion. The background is a dark blue-purple gradient (#0a0a1a to #1a1a3a).

**Initial Trie State**:
- Root node (empty, central position)
- Words already inserted: "app", "apple"
- Tree structure:
  - root → 'a' → 'p' → 'p' (word-end) → 'l' → 'e' (word-end)

**Insert "application" Animation**:

Step 1: Start at root
- Root node highlights
- "Inserting: application"

Step 2: Follow 'a'
- Edge to 'a' glows cyan
- Move to 'a' node

Step 3: Follow 'p'
- Edge to 'p' glows
- Move to first 'p'

Step 4: Follow 'p'
- Edge to second 'p' glows
- This node is word-end for "app"

Step 5: Follow 'l'
- Edge to 'l' glows
- Move to 'l'

Step 6: Create 'i'
- No 'i' child exists
- New node 'i' created (animation: node appears)
- Edge created

Step 7-11: Create remaining nodes
- 'c', 'a', 't', 'i', 'o', 'n' created
- Each with creation animation

Step 12: Mark word-end
- Final 'n' node gets gold ring
- "application" inserted successfully

**Visual Elements**:
- Spherical character nodes
- Character labels on nodes
- Gold rings for word-ends
- Cyan path highlighting
- Node creation animations
- Tree branching structure

---

## Prompt 2: Trie Search and Prefix Operations

Generate a 360-degree, interactive 3D scene demonstrating Trie search and prefix operations.

**Trie Contents**:
- Words: "apple", "app", "application", "apply", "apt", "bat", "bath"

**Search "apply" (Success)**:

Step 1-5: Follow path a → p → p → l → y
- Each edge glows cyan as traversed
- Nodes highlight in sequence

Step 6: Check word-end
- 'y' node has gold ring
- Green success glow
- "Found: apply"

**Search "apex" (Failure)**:

Step 1-3: Follow path a → p → e
- Wait, no 'e' child of second 'p'
- At 'p', children are: 'p', 'l', 't'
- Red flash at 'p' node
- "Not found: apex"

**Prefix Search "app"**:

Step 1-3: Follow path a → p → p
- Reach "app" node

Step 4: Collect subtree words
- Subtree highlights (all descendants)
- Words found: "app", "apple", "application", "apply"
- Results displayed

**Visual Elements**:
- Path traversal animation
- Success/failure indicators
- Subtree highlighting
- Word collection display
- Character matching visualization

---

## Prompt 3: Segment Tree Structure

Generate a 360-degree, interactive 3D scene demonstrating Segment Tree structure for range sums.

**Array Setup**:
- Array: [1, 3, 5, 7, 9, 11]
- 6 elements, indices 0-5

**Tree Structure**:
```
                [36] (0-5)
              /          \
        [9] (0-2)      [27] (3-5)
        /     \         /      \
    [4](0-1) [5](2)  [16](3-4) [11](5)
    /    \           /     \
  [1](0) [3](1)   [7](3)  [9](4)
```

**Visualization**:
- Array as base row of tiles
- Tree nodes floating above
- Each node shows: value and range
- Lines connecting nodes to children
- Lines connecting leaves to array elements

**Node Information**:
- Root: sum=36, range=[0,5]
- Level 1: sums 9 and 27
- Level 2: sums 4, 5, 16, 11
- Leaves: individual elements

**Visual Elements**:
- Array base layer
- Pyramid tree structure
- Range labels on nodes
- Sum values displayed
- Parent-child connections
- Leaf-to-array connections

---

## Prompt 4: Segment Tree Range Query

Generate a 360-degree, interactive 3D scene demonstrating a range sum query on a Segment Tree.

**Setup**:
- Array: [1, 3, 5, 7, 9, 11]
- Query: sum(1, 4) - sum of elements at indices 1-4

**Query Animation**:

Step 1: Highlight query range
- Array positions 1-4 glow
- "Query: sum[1, 4]"

Step 2: Start at root [0-5]
- Root highlighted
- Range [0-5] contains [1-4] but not equal
- Split query

Step 3: Check left child [0-2]
- Range [0-2] overlaps [1-4]
- Need to go deeper

Step 4: Check [0-1]
- Range [0-1] partially overlaps [1-4]
- Only index 1 is in query
- Go to leaf [1] = 3
- Add 3 to result

Step 5: Check [2]
- Range [2] is within [1-4]
- Add 5 to result
- Result so far: 8

Step 6: Check right child [3-5]
- Range [3-5] overlaps [1-4]

Step 7: Check [3-4]
- Range [3-4] is completely within [1-4]
- Add 16 to result
- Result: 24

Step 8: Check [5]
- Range [5] is outside [1-4]
- Skip

Step 9: Final result
- sum[1,4] = 3 + 5 + 16 = 24
- Verify: 3 + 5 + 7 + 9 = 24

**Visual Elements**:
- Query range highlighting
- Node traversal animation
- Partial/complete overlap indicators
- Value accumulation display
- Result calculation

---

## Prompt 5: Segment Tree Point Update

Generate a 360-degree, interactive 3D scene demonstrating a point update on a Segment Tree.

**Setup**:
- Array: [1, 3, 5, 7, 9, 11]
- Update: set index 2 to 10 (was 5)

**Update Animation**:

Step 1: Highlight update position
- Array position 2 glows
- "Update: arr[2] = 10"

Step 2: Find leaf node
- Traverse to leaf [2]
- Path: root → left → right

Step 3: Update leaf
- Leaf value changes: 5 → 10
- Difference: +5

Step 4: Propagate to parent [0-2]
- Old value: 9
- New value: 9 + 5 = 14
- Node updates with animation

Step 5: Propagate to root [0-5]
- Old value: 36
- New value: 36 + 5 = 41
- Root updates

Step 6: Update complete
- All affected nodes show new values
- Update wave visualization
- "Update complete"

**Visual Elements**:
- Update position highlighting
- Leaf modification animation
- Upward propagation wave
- Value change indicators
- Before/after comparison

---

## Prompt 6: Fenwick Tree Structure

Generate a 360-degree, interactive 3D scene demonstrating Fenwick Tree (Binary Indexed Tree) structure.

**Array Setup**:
- Original array: [3, 2, -1, 6, 5, 4, -3, 3, 7, 2]
- Indices: 1-10 (1-indexed)

**Fenwick Tree Array**:
- BIT[1] = arr[1] = 3
- BIT[2] = arr[1] + arr[2] = 5
- BIT[3] = arr[3] = -1
- BIT[4] = arr[1] + arr[2] + arr[3] + arr[4] = 10
- BIT[5] = arr[5] = 5
- BIT[6] = arr[5] + arr[6] = 9
- BIT[7] = arr[7] = -3
- BIT[8] = sum of arr[1..8] = 19
- etc.

**Responsibility Visualization**:
- Each position covers range based on LSB
- Position 1 (binary 0001): covers 1 element
- Position 2 (binary 0010): covers 2 elements
- Position 4 (binary 0100): covers 4 elements
- Position 8 (binary 1000): covers 8 elements

**Connection Lines**:
- Show which positions contribute to each BIT value
- Binary representation displayed
- LSB highlighted

**Visual Elements**:
- Original array row
- BIT array row
- Responsibility range brackets
- Binary index labels
- Connection lines
- LSB indicators

---

## Prompt 7: Fenwick Tree Update Operation

Generate a 360-degree, interactive 3D scene demonstrating a Fenwick Tree point update.

**Setup**:
- BIT array (10 elements)
- Update: add 5 to position 3

**Update Path Calculation**:
- Start: i = 3 (binary: 0011)
- LSB(3) = 1
- Next: 3 + 1 = 4 (binary: 0100)
- LSB(4) = 4
- Next: 4 + 4 = 8 (binary: 1000)
- LSB(8) = 8
- Next: 8 + 8 = 16 > 10, stop

**Update Animation**:

Step 1: Start at position 3
- Position 3 highlights
- "Update position 3 by +5"
- Binary: 0011, LSB = 1

Step 2: Update BIT[3]
- BIT[3] += 5
- Value changes
- Green glow

Step 3: Move to position 4
- 3 + LSB(3) = 4
- Connection line glows
- Binary: 0100, LSB = 4

Step 4: Update BIT[4]
- BIT[4] += 5
- Value changes

Step 5: Move to position 8
- 4 + LSB(4) = 8
- Connection line glows
- Binary: 1000, LSB = 8

Step 6: Update BIT[8]
- BIT[8] += 5
- Value changes

Step 7: Complete
- 8 + 8 = 16 > 10
- Update complete
- All affected positions highlighted

**Visual Elements**:
- Update path animation
- Binary representation display
- LSB calculation
- Value change indicators
- Connection highlighting

---

## Prompt 8: Fenwick Tree Query Operation

Generate a 360-degree, interactive 3D scene demonstrating a Fenwick Tree prefix sum query.

**Setup**:
- BIT array with values
- Query: prefix sum up to index 7

**Query Path Calculation**:
- Start: i = 7 (binary: 0111)
- LSB(7) = 1
- Add BIT[7], move to 7 - 1 = 6
- LSB(6) = 2
- Add BIT[6], move to 6 - 2 = 4
- LSB(4) = 4
- Add BIT[4], move to 4 - 4 = 0
- Stop at 0

**Query Animation**:

Step 1: Start at position 7
- Position 7 highlights
- "Query: prefix_sum(7)"
- Binary: 0111, LSB = 1

Step 2: Add BIT[7]
- result = BIT[7]
- Value accumulated
- Gold glow

Step 3: Move to position 6
- 7 - LSB(7) = 6
- Connection line glows
- Binary: 0110, LSB = 2

Step 4: Add BIT[6]
- result += BIT[6]
- Running total shown

Step 5: Move to position 4
- 6 - LSB(6) = 4
- Binary: 0100, LSB = 4

Step 6: Add BIT[4]
- result += BIT[4]
- Running total updated

Step 7: Complete
- 4 - 4 = 0
- Query complete
- "prefix_sum(7) = result"

**Range Sum**:
- sum(3, 7) = prefix_sum(7) - prefix_sum(2)
- Show both query paths
- Subtraction visualization

**Visual Elements**:
- Query path animation
- Binary representation
- Value accumulation
- Running total display
- Range sum calculation

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
- Show binary representations for Fenwick Tree operations
- Display time complexity for each operation
