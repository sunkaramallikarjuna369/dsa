# Visual Design: Advanced Data Structures

## Environment Overview

The Advanced Data Structures world presents three specialized tree structures, each with its own visual metaphor. The environment emphasizes the hierarchical nature of these structures and how they enable efficient operations.

### Background and Atmosphere

The scene is set in a high-tech data center with a dark blue-purple gradient background (#0a0a1a to #1a1a3a). Holographic displays show the structures. Neon accents highlight active operations. The atmosphere conveys advanced computation.

### Lighting

Active nodes glow with their operation color. Trie paths glow cyan for searches. Segment tree query nodes glow gold. Fenwick tree update paths glow green. Inactive nodes have subtle ambient lighting.

### Camera Behavior

The camera can orbit 360 degrees around each structure, zoom to see individual nodes, and follow operations as they traverse the tree. For Tries, the camera can follow word paths. For Segment/Fenwick trees, the camera can show the array-tree relationship.

### Interaction Ideas

Clicking a node shows its value and range. Users can input custom operations. Speed controls adjust animation pace. Toggle between different views (tree vs array). Hover shows node metadata.

---

## Sub-Concept 1: Trie Structure

### 3D Metaphor

A Trie is visualized as a tree of character nodes where paths from root spell out words.

**Tree Structure**:
- Root node at center (no character)
- Child nodes branch outward
- Each edge labeled with a character
- Word endpoints marked with special glow

**Node Design**:
- Spherical nodes
- Character displayed on node
- Word-end nodes have gold ring
- Depth indicated by vertical position

**Path Visualization**:
- Paths glow when traversed
- Common prefixes share paths
- Divergence points highlighted
- Word completion indicated

### Visual Elements

- Character-labeled nodes
- Branching tree structure
- Word-end markers
- Path highlighting
- Prefix sharing visualization

---

## Sub-Concept 2: Trie Operations

### 3D Metaphor

Trie operations are visualized as traversing and modifying the character tree.

**Insert Operation**:
- Start at root
- Follow existing path for matching characters
- Create new nodes for new characters
- Mark final node as word-end
- New nodes appear with animation

**Search Operation**:
- Start at root
- Follow path character by character
- Path glows as traversed
- Success: reach word-end node (green glow)
- Failure: path doesn't exist (red flash)

**Prefix Search**:
- Follow prefix path
- Collect all words in subtree
- Subtree highlights
- Results displayed

### Visual Elements

- Path traversal animation
- Node creation animation
- Word-end marking
- Success/failure indicators
- Subtree highlighting

---

## Sub-Concept 3: Segment Tree Structure

### 3D Metaphor

A Segment Tree is visualized as a pyramid of nodes layered over an array.

**Array Base**:
- Original array as row of tiles
- Each tile shows element value
- Array indices labeled

**Tree Layers**:
- Leaf nodes directly above array elements
- Internal nodes aggregate children
- Root at top covers entire range
- Each node shows its range and value

**Range Visualization**:
- Each node's range shown as bracket
- Parent range = union of children
- Color coding by level

### Visual Elements

- Array base layer
- Pyramid tree structure
- Range brackets
- Aggregate values
- Level coloring

---

## Sub-Concept 4: Segment Tree Operations

### 3D Metaphor

Segment Tree operations are visualized as traversing the pyramid to answer queries or propagate updates.

**Range Query**:
- Query range highlighted on array
- Traverse tree to find covering nodes
- Minimal set of nodes glow
- Values combine for answer
- Result displayed

**Point Update**:
- Updated position highlighted
- Leaf node updated
- Changes propagate upward
- All affected nodes update
- Wave of updates visible

**Range Update (Lazy)**:
- Range highlighted
- Lazy values stored at nodes
- Propagation on demand
- Pending updates shown differently

### Visual Elements

- Query range highlighting
- Node selection animation
- Value combination
- Update propagation wave
- Lazy value indicators

---

## Sub-Concept 5: Fenwick Tree Structure

### 3D Metaphor

A Fenwick Tree is visualized as an array with binary-indexed connections.

**Array Representation**:
- Array of values
- Each position has responsibility range
- Connections based on binary representation
- Position i responsible for range based on lowest set bit

**Connection Visualization**:
- Lines connecting related positions
- Update path: i, i + LSB(i), ...
- Query path: i, i - LSB(i), ...
- Binary representation shown

**Responsibility Ranges**:
- Each position covers specific range
- Range size = lowest set bit
- Overlapping responsibilities shown

### Visual Elements

- Array with values
- Binary index labels
- Connection lines
- Responsibility ranges
- LSB indicators

---

## Sub-Concept 6: Fenwick Tree Operations

### 3D Metaphor

Fenwick Tree operations are visualized as following binary-indexed paths.

**Point Update**:
- Start at position i
- Update value
- Move to i + LSB(i)
- Continue until out of bounds
- Path glows green

**Prefix Sum Query**:
- Start at position i
- Accumulate value
- Move to i - LSB(i)
- Continue until 0
- Path glows gold

**Range Sum**:
- prefix(r) - prefix(l-1)
- Two query paths shown
- Subtraction visualized

### Visual Elements

- Update path animation
- Query path animation
- Value accumulation
- Binary arithmetic display
- Range calculation

---

## Color Palette

| Element | Color | Hex Code |
|---------|-------|----------|
| Background | Deep Blue | #0a0a1a |
| Trie Node | Cyan | #00ffff |
| Word End | Gold | #ffd700 |
| Trie Path | Electric Blue | #00d4ff |
| Segment Node | Purple | #9b59b6 |
| Query Range | Orange | #e67e22 |
| Update Wave | Green | #2ecc71 |
| Fenwick Array | Teal | #1abc9c |
| Update Path | Lime | #00ff00 |
| Query Path | Yellow | #f1c40f |
| Inactive | Gray | #4a4a4a |
| Array Element | White | #ffffff |

---

## Animation Timing

- Trie character traversal: 300ms per character
- Node creation: 400ms
- Word-end marking: 300ms
- Segment tree query step: 250ms
- Value combination: 200ms
- Update propagation: 200ms per level
- Fenwick update step: 300ms
- Fenwick query step: 300ms
- Binary calculation display: 400ms
- Path highlighting: 200ms
- Camera transitions: 500ms ease-in-out
