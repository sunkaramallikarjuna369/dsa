# 3D Generator Prompts: Trees and Binary Search Trees

These prompts are designed for use with 3D generation tools such as Three.js, WebGL, Blender scripting agents, or AI-powered 3D scene generators. Each prompt provides sufficient detail to create an educational, interactive 360-degree visualization.

---

## Prompt 1: Binary Tree Structure

Generate a 360-degree, interactive 3D scene showing a binary tree structure floating in a deep space environment. The background is dark blue-black (#0a0a1a) with subtle star particles.

Create a binary tree with 7 nodes arranged in a complete binary tree pattern:
- Root (value 50) at the top, glowing bright white (#ffffff), slightly larger than other nodes
- Level 1: Left child (30), Right child (70)
- Level 2: Four leaf nodes (20, 40, 60, 80)

**Node Design**:
- Spheres with 20cm diameter (root 25cm)
- Soft cyan glow (#4ecdc4) with inner illumination
- Value displayed on sphere surface in white text
- Leaf nodes have subtle pulsing animation

**Edge Design**:
- Glowing cylindrical connections (5cm diameter)
- Left edges tinted blue (#5dade2)
- Right edges tinted orange (#f5b041)
- Edges angle 30 degrees downward from parent

**Spatial Arrangement**:
- Vertical spacing: 80cm between levels
- Horizontal spread: Doubles at each level (40cm, 80cm, 160cm from center)
- Tree centered in view

Include interactive elements:
- Clicking a node shows: value, depth, height, parent, children
- Hovering highlights the path from root to that node
- Tree property panel showing: total nodes, height, leaf count

The camera can orbit 360 degrees, zoom in/out, and has preset views: front, side, top-down.

---

## Prompt 2: BST Ordering Property Visualization

Generate a 360-degree, interactive 3D scene demonstrating the Binary Search Tree ordering property. Create a BST with values [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45].

**Color Gradient Based on Value**:
- Minimum value (10): Deep blue (#3498db)
- Maximum value (80): Warm orange (#e67e22)
- Intermediate values: Gradient through green and yellow
- This creates a visual spectrum where in-order traversal follows the rainbow

**BST Property Visualization**:
- Left subtrees contain cooler colors (smaller values)
- Right subtrees contain warmer colors (larger values)
- At each node, left children are visibly "cooler" than parent
- At each node, right children are visibly "warmer" than parent

**Interactive Features**:
- "Verify BST" button that checks and highlights any violations
- Clicking a node shows: "All left descendants < this < All right descendants"
- In-order traversal button that visits nodes in color order (blue to orange)
- Value range display for each subtree on hover

Include a gradient legend bar showing the value-to-color mapping. Add an "Insert Value" panel where users can add new nodes and see them placed according to BST rules with appropriate coloring.

---

## Prompt 3: Tree Traversal Animations

Generate a 360-degree, interactive 3D scene showing all four tree traversal types on a BST with values [50, 30, 70, 20, 40, 60, 80].

Create a control panel with four traversal buttons, each triggering a different animated path through the tree:

**In-Order Traversal (Left, Root, Right)**:
- Green glowing path (#2ecc71)
- Visits: 20 → 30 → 40 → 50 → 60 → 70 → 80
- Path zigzags: descends left fully, visits, then right
- Output panel shows values in sorted order
- Label: "In-Order: Sorted output for BST"

**Pre-Order Traversal (Root, Left, Right)**:
- Blue glowing path (#3498db)
- Visits: 50 → 30 → 20 → 40 → 70 → 60 → 80
- Path visits current node before descending
- Label: "Pre-Order: Copy tree structure"

**Post-Order Traversal (Left, Right, Root)**:
- Purple glowing path (#9b59b6)
- Visits: 20 → 40 → 30 → 60 → 80 → 70 → 50
- Path visits children before parent
- Label: "Post-Order: Delete tree safely"

**Level-Order Traversal (BFS)**:
- Orange glowing path (#e67e22)
- Visits: 50 → 30 → 70 → 20 → 40 → 60 → 80
- Path sweeps horizontally across each level
- Queue visualization below tree showing frontier
- Label: "Level-Order: Breadth-first exploration"

**Animation Features**:
- Speed slider (0.5x to 3x)
- Pause/resume button
- Step-by-step mode
- Visit order numbers appear on nodes
- Output sequence builds as nodes are visited
- Path trails fade after 2 seconds

---

## Prompt 4: BST Insert Operation

Generate a 360-degree, interactive 3D scene demonstrating BST insertion. Start with a BST containing [50, 30, 70, 20, 40].

**Insert Animation for value 35**:
1. Value 35 appears as a glowing sphere above the root
2. Comparison at root (50): 35 < 50, go LEFT
   - Comparison indicator: "35 < 50 → LEFT"
   - Path to left child glows
3. Comparison at node 30: 35 > 30, go RIGHT
   - Comparison indicator: "35 > 30 → RIGHT"
   - Path to right child glows
4. Comparison at node 40: 35 < 40, go LEFT
   - Comparison indicator: "35 < 40 → LEFT"
   - Left child is NULL
5. New node materializes at the empty position
   - Node creation animation with particle effect
   - Edge connects to parent (40)
   - Tree structure updates

**Visual Elements**:
- Descending value sphere with trail
- Comparison results at each node (< or >)
- Direction indicators (LEFT/RIGHT arrows)
- Path highlighting showing route taken
- Final position celebration effect

**Interactive Panel**:
- Input field for new value
- "Insert" button to trigger animation
- "Random Insert" for demonstration
- Insert history log

---

## Prompt 5: BST Delete Operation

Generate a 360-degree, interactive 3D scene demonstrating all three BST deletion cases. Create a BST with values [50, 30, 70, 20, 40, 60, 80, 35, 45].

**Case 1: Delete Leaf Node (20)**
1. Search animation finds node 20
2. Node 20 highlighted as target
3. "Case 1: Leaf node - simply remove"
4. Node 20 fades away with particle dissolve
5. Parent's (30) left pointer becomes null

**Case 2: Delete Node with One Child (40, which has children 35 and 45)**
Actually, let's use a simpler example. Delete node 60 (which has no children in this tree, so let's adjust):
Create tree where 60 has one child (65):
1. Search animation finds node 60
2. "Case 2: One child - bypass node"
3. Node 60 fades
4. Child (65) moves up to take 60's position
5. Edge from 70 reconnects to 65

**Case 3: Delete Node with Two Children (30)**
1. Search animation finds node 30
2. "Case 3: Two children - find successor"
3. In-order successor search: Go right to 40, then left to 35
4. Successor (35) highlighted
5. Value 35 copies to node 30's position (value swap animation)
6. Original successor node (35) is deleted (now a leaf or one-child case)
7. Tree structure updates

**Control Panel**:
- Node selector dropdown
- "Delete" button
- Case explanation panel
- Step-by-step mode toggle

---

## Prompt 6: Balanced vs Unbalanced BST Comparison

Generate a 360-degree, interactive 3D scene with split view comparing balanced and unbalanced BSTs.

**Left Side: Unbalanced BST**
Insert values in order: [10, 20, 30, 40, 50, 60, 70]
- Results in a degenerate tree (essentially a linked list)
- Very tall and narrow (height = 6)
- All nodes chain to the right
- "Unbalanced" label with warning indicator
- Search for 70: Show 7 comparisons needed
- Complexity indicator: "O(n) operations"

**Right Side: Balanced BST**
Same values but balanced: [40, 20, 60, 10, 30, 50, 70]
- Compact, symmetric structure
- Minimal height (height = 2)
- "Balanced" label with optimal indicator
- Search for 70: Show 3 comparisons needed
- Complexity indicator: "O(log n) operations"

**Comparison Features**:
- Height comparison: 6 vs 2
- Search path length comparison
- Simultaneous search animation on both trees
- Performance graph showing operation counts

**Rotation Demo** (on balanced side):
- "Trigger Imbalance" button adds nodes to unbalance
- Balance factor display on each node
- When |balance factor| > 1, rotation triggers:
  - Left rotation animation
  - Right rotation animation
  - Nodes smoothly transition to new positions
  - Edges reconnect with animation

---

## Prompt 7: Tree from Sorted Array

Generate a 360-degree, interactive 3D scene showing how to build a balanced BST from a sorted array.

**Input**: Sorted array [10, 20, 30, 40, 50, 60, 70] displayed as a horizontal row of blocks.

**Algorithm Visualization**:
1. "Find middle element (40) - this becomes root"
   - Middle element (40) highlights and rises to become root
2. "Recursively build left subtree from [10, 20, 30]"
   - Left portion highlights
   - Middle (20) becomes left child of root
   - 10 becomes left child of 20
   - 30 becomes right child of 20
3. "Recursively build right subtree from [50, 60, 70]"
   - Right portion highlights
   - Middle (60) becomes right child of root
   - 50 becomes left child of 60
   - 70 becomes right child of 60

**Animation Sequence**:
- Array elements lift and position themselves in tree structure
- Recursive calls shown with indentation/depth indicator
- Each subtree construction is a mini-animation
- Final tree is perfectly balanced

**Interactive Features**:
- Custom array input
- Step-by-step execution
- Recursion depth visualization
- "Why middle?" explanation tooltip

---

## General Requirements for All Prompts

- All scenes must support 360-degree camera orbit and zoom in/out functionality
- Include educational labels with readable fonts (minimum 14pt equivalent in 3D space)
- Use color coding consistently across all scenes as defined in the color palette
- Ensure interactive elements have clear hover states and click feedback
- Animations should be smooth (60fps target) with adjustable speed controls
- Include accessibility considerations: high contrast mode option, colorblind-friendly palette alternative
- All text labels should remain readable from any camera angle (billboard text or smart orientation)
- Export scenes in formats compatible with web embedding (glTF, WebGL-ready)
- Include corresponding Python code snippets that highlight during relevant animation steps
- Tree structures should cast soft shadows for depth perception
