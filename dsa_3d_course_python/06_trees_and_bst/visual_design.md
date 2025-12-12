# Visual Design: Trees and Binary Search Trees

## Environment Overview

The Trees world is set in a vast vertical space where tree structures grow downward from the ceiling. The environment emphasizes the hierarchical nature of trees and the ordering property of BSTs through spatial arrangement and color coding.

### Background and Atmosphere

The scene is a deep space environment with subtle star particles. The tree structure floats in the center, with the root at the top and branches extending downward. A soft gradient from deep blue (top) to purple (bottom) provides depth perception. Nodes glow with inner light, and edges are rendered as glowing connections.

### Lighting

Each node emits its own soft glow. The root node glows brightest as the entry point. Active nodes during operations glow with increased intensity. Traversal paths leave temporary light trails. The BST color gradient (blue for small values, orange for large) provides visual ordering cues.

### Camera Behavior

The camera can orbit 360 degrees around the tree, zoom in to examine individual nodes, and follow traversal paths. A "bird's eye" view shows the overall structure from above. The camera can also track insertion and deletion operations as they navigate through the tree.

### Interaction Ideas

Clicking a node reveals its value, parent, and children. Dragging allows rotation of the entire tree. Hovering shows the path from root to that node. Controls for triggering traversals with adjustable speed. Insert/delete panels for modifying the tree.

---

## Sub-Concept 1: Binary Tree Structure

### 3D Metaphor

A binary tree is visualized as a hierarchical structure of glowing spheres connected by luminous branches. The root sphere is at the top, larger and brighter than other nodes. Each node can have up to two children extending downward and outward.

**Node Representation**:
- Spheres of uniform size (except root which is slightly larger)
- Value displayed on the sphere surface
- Left children positioned to the left and below
- Right children positioned to the right and below
- Leaf nodes have a subtle pulsing effect

**Edge Representation**:
- Glowing cylindrical connections between parent and child
- Edges angle downward from parent to child
- Left edges have a slight blue tint
- Right edges have a slight orange tint

**Tree Properties Visualization**:
- Height: Vertical distance from root to deepest leaf
- Depth: Distance from root to any node (shown on hover)
- Level: Horizontal bands showing nodes at same depth

### Visual Elements

- Glowing sphere nodes with value labels
- Branching edges with directional coloring
- Level indicators (horizontal planes)
- Height measurement display
- Node count and leaf count displays

---

## Sub-Concept 2: BST Ordering Property

### 3D Metaphor

The BST ordering property is visualized through a color gradient. Nodes with smaller values glow with cool colors (blue), while nodes with larger values glow with warm colors (orange/red). This creates a visual gradient where in-order traversal follows the color spectrum.

**Color Mapping**:
- Minimum value: Deep blue (#3498db)
- Middle values: Green/yellow transition
- Maximum value: Warm orange (#e67e22)
- The gradient is normalized to the current tree's value range

**Ordering Visualization**:
- Left subtree: Cooler colors (all values < parent)
- Right subtree: Warmer colors (all values > parent)
- In-order traversal follows the rainbow from blue to orange

**Invalid BST Detection**:
- Nodes violating BST property flash red
- Violation edges are highlighted with warning color
- Tooltip explains the violation

### Visual Elements

- Color-coded nodes based on value
- Gradient legend showing value-to-color mapping
- Subtree boundary indicators
- BST property verification display

---

## Sub-Concept 3: Tree Traversals

### 3D Metaphor

Each traversal type is visualized as a glowing path that visits nodes in a specific order. The path leaves a temporary trail showing the traversal route, and visited nodes light up sequentially.

**In-Order Traversal (Left, Root, Right)**:
- Path zigzags: descends left, visits node, descends right
- For BST, visits nodes in sorted order
- Trail color: Green (#2ecc71)
- Output sequence displayed as nodes are visited

**Pre-Order Traversal (Root, Left, Right)**:
- Path visits current node first, then descends
- Useful for copying tree structure
- Trail color: Blue (#3498db)
- Shows "process before children" pattern

**Post-Order Traversal (Left, Right, Root)**:
- Path descends to leaves first, visits on way up
- Useful for deletion (children before parent)
- Trail color: Purple (#9b59b6)
- Shows "process after children" pattern

**Level-Order Traversal (BFS)**:
- Path sweeps horizontally across each level
- Uses queue visualization below the tree
- Trail color: Orange (#e67e22)
- Shows breadth-first exploration

### Visual Elements

- Animated traversal paths with trails
- Node visit order numbers
- Output sequence display
- Traversal type indicator
- Speed control for animation

---

## Sub-Concept 4: BST Operations

### 3D Metaphor

BST operations (insert, search, delete) are visualized as animated journeys through the tree, with the path taken highlighted and the operation result clearly shown.

**Insert Operation**:
1. New value appears above the root
2. Comparison at root: go left if smaller, right if larger
3. Path glows as the value descends
4. At null position, new node materializes and connects
5. Tree rebalances visually if needed

**Search Operation**:
1. Search value appears as a probe above root
2. Probe descends, comparing at each node
3. Matching comparisons glow green, mismatches glow briefly
4. Found: Target node pulses green
5. Not found: Probe reaches null, red indicator

**Delete Operation**:
1. Target node is located (search animation)
2. Case 1 (Leaf): Node simply fades away
3. Case 2 (One child): Node fades, child moves up to take its place
4. Case 3 (Two children): 
   - In-order successor is found (rightmost in left subtree or leftmost in right)
   - Successor value copies to target
   - Successor node is deleted (recursively)

### Visual Elements

- Animated value/probe movement
- Comparison result indicators
- Path highlighting
- Node transformation animations
- Successor finding visualization

---

## Sub-Concept 5: Tree Balancing Concepts

### 3D Metaphor

Unbalanced vs balanced trees are shown side by side to illustrate the importance of balancing. Rotations are visualized as smooth 3D transformations.

**Unbalanced Tree**:
- Degenerates toward a linked list
- Very tall and narrow
- Operations take O(n) time
- "Danger zone" indicator for height

**Balanced Tree**:
- Compact, symmetric structure
- Minimal height for given nodes
- Operations take O(log n) time
- "Optimal" indicator

**Rotation Animations**:
- Left rotation: Right child becomes new root, old root becomes left child
- Right rotation: Left child becomes new root, old root becomes right child
- Nodes smoothly transition to new positions
- Edges reconnect with animation

**AVL Balance Factor**:
- Each node shows balance factor (-1, 0, +1 for balanced)
- Unbalanced nodes (|bf| > 1) highlighted in red
- Rotation triggers when balance factor exceeds threshold

### Visual Elements

- Side-by-side balanced/unbalanced comparison
- Height and balance factor displays
- Rotation animation with smooth transitions
- Performance comparison (O(n) vs O(log n))
- Balance indicator per node

---

## Color Palette

| Element | Color | Hex Code |
|---------|-------|----------|
| Background | Deep Space Blue | #0a0a1a |
| Root node | Bright White | #ffffff |
| Regular node | Soft Cyan | #4ecdc4 |
| BST small values | Cool Blue | #3498db |
| BST large values | Warm Orange | #e67e22 |
| Left edge | Blue tint | #5dade2 |
| Right edge | Orange tint | #f5b041 |
| In-order path | Green | #2ecc71 |
| Pre-order path | Blue | #3498db |
| Post-order path | Purple | #9b59b6 |
| Level-order path | Orange | #e67e22 |
| Found/success | Bright Green | #27ae60 |
| Not found/error | Red | #e74c3c |
| Unbalanced warning | Warning Red | #c0392b |

---

## Animation Timing

- Node insertion descent: 400ms per level
- Search probe movement: 300ms per level
- Node deletion fade: 500ms
- Successor swap: 600ms
- Traversal visit per node: 300ms (adjustable)
- Rotation animation: 800ms
- Tree rebalancing: 600ms
- Camera transitions: 500ms ease-in-out
- Path trail fade: 2000ms
