# Visual Design: Graphs and Traversals

## Environment Overview

The Graphs world presents a 3D space filled with floating nodes connected by glowing edges. The environment emphasizes the network structure of graphs and provides clear visualizations of traversal algorithms.

### Background and Atmosphere

The scene is set in a deep space environment with subtle nebula effects in dark blue and purple. Nodes float as glowing spheres, and edges are luminous beams connecting them. The vastness of space emphasizes the potentially infinite nature of graph structures.

### Lighting

Nodes emit soft ambient light, with visited nodes glowing brighter. Edges have a subtle glow that intensifies when traversed. The current node in traversal has a spotlight effect. Different traversal algorithms use distinct color schemes.

### Camera Behavior

The camera can orbit 360 degrees around the graph, zoom to individual nodes, and follow traversal paths. A "graph overview" mode shows the entire structure, while "traversal mode" follows the algorithm's progress. The camera can also switch between different graph representations.

### Interaction Ideas

Clicking a node shows its value, neighbors, and degree. Dragging allows graph rotation. Users can add/remove edges interactively. Traversal controls include start, pause, step, and speed adjustment.

---

## Sub-Concept 1: Graph Structure and Representations

### 3D Metaphor

The graph is visualized as floating cities (nodes) connected by roads (edges). Two representation views are available: adjacency list view and adjacency matrix view.

**Node Visualization**:
- Spheres of uniform size (20cm diameter)
- Node label displayed on surface
- Color indicates state: unvisited (gray), visiting (yellow), visited (green)
- Degree shown as small number badge

**Edge Visualization**:
- Glowing beams connecting nodes
- Undirected: equal glow in both directions
- Directed: arrow indicator showing direction
- Weighted: thickness or brightness indicates weight

**Adjacency List View**:
- Each node has a trailing list of neighbor labels
- Lists float beside their source nodes
- Connections shown as lines from list items to actual nodes

**Adjacency Matrix View**:
- 2D grid floating in space
- Rows and columns labeled with node names
- Cells glow if edge exists (1) or dark if not (0)
- Clicking a cell highlights corresponding edge

### Visual Elements

- Floating sphere nodes with labels
- Glowing beam edges
- Adjacency list panels
- Adjacency matrix grid
- Representation toggle button

---

## Sub-Concept 2: Breadth-First Search (BFS)

### 3D Metaphor

BFS is visualized as an expanding wavefront from the source node. Like ripples in water, each wave represents one level of distance from the source.

**Wavefront Animation**:
- Source node pulses and emits first wave
- Wave expands to all direct neighbors simultaneously
- Each subsequent wave reaches the next level
- Wave color indicates distance level (gradient from blue to red)

**Queue Visualization**:
- Queue displayed as a horizontal line of nodes
- New nodes enter from the right
- Processing node exits from the left
- Queue shrinks and grows as algorithm progresses

**Level Indicators**:
- Concentric rings around source showing distance levels
- Nodes at same level have same ring color
- Level numbers displayed on rings

**Path Tracking**:
- Parent pointers shown as dim arrows
- Shortest path to any node can be highlighted
- Path length displayed when node selected

### Visual Elements

- Expanding wave animation
- Queue visualization bar
- Level rings
- Parent pointer arrows
- Distance labels on nodes

---

## Sub-Concept 3: Depth-First Search (DFS)

### 3D Metaphor

DFS is visualized as a single exploration beam that dives deep into the graph, backtracking when it hits dead ends.

**Exploration Beam**:
- Bright beam leaves source node
- Follows one path as deep as possible
- Beam color changes as it goes deeper (blue to purple)
- Trail left behind shows visited path

**Backtracking Animation**:
- When dead end reached, beam retraces path
- Backtracked edges dim but remain visible
- Beam returns to last node with unexplored neighbors
- New exploration continues from there

**Stack Visualization**:
- Vertical stack displayed beside graph
- Current path shown as stacked nodes
- Pop animation when backtracking
- Push animation when going deeper

**Discovery vs Finish Times**:
- Discovery time shown when node first visited
- Finish time shown when all descendants explored
- Timestamps displayed as small badges

### Visual Elements

- Exploration beam with trail
- Backtracking animation
- Stack visualization
- Discovery/finish time badges
- Recursion depth indicator

---

## Sub-Concept 4: Connected Components

### 3D Metaphor

Connected components are visualized by coloring each component differently. Nodes that can reach each other share the same color.

**Component Coloring**:
- Each connected component gets a unique color
- Colors are distinct and vibrant
- Edges within a component match the component color
- Isolated nodes have their own color

**Component Discovery**:
- BFS/DFS from unvisited node discovers one component
- Component lights up as it's discovered
- Process repeats for remaining unvisited nodes
- Final result shows all components in different colors

**Component Statistics**:
- Component count displayed
- Size of each component shown
- Largest/smallest component highlighted
- Connectivity percentage calculated

### Visual Elements

- Multi-colored components
- Component discovery animation
- Statistics panel
- Component size indicators
- Connectivity visualization

---

## Sub-Concept 5: Shortest Path (Unweighted)

### 3D Metaphor

Finding the shortest path using BFS is visualized as waves finding the target, then tracing back the optimal route.

**Path Finding Animation**:
- BFS waves expand from source
- Target node highlighted
- When wave reaches target, path is found
- Optimal path traced back using parent pointers

**Path Highlighting**:
- Shortest path edges glow bright gold
- Path nodes pulse with success effect
- Path length displayed prominently
- Alternative paths shown dimly for comparison

**Distance Visualization**:
- All nodes show distance from source
- Gradient coloring by distance
- Unreachable nodes marked differently
- Distance comparison between paths

### Visual Elements

- BFS wave animation
- Golden path highlight
- Distance labels
- Path comparison view
- Unreachable node indicators

---

## Sub-Concept 6: Directed Graphs and Cycles

### 3D Metaphor

Directed graphs have edges with arrows showing direction. Cycle detection is visualized by highlighting back edges that create cycles.

**Directed Edge Visualization**:
- Arrows on edges show direction
- One-way vs two-way edges clearly distinguished
- In-degree and out-degree shown for each node
- Edge direction affects traversal

**Cycle Detection**:
- DFS explores graph
- Back edge (to ancestor) indicates cycle
- Cycle highlighted in red
- Cycle path traced and displayed

**Topological Sort**:
- For DAGs (no cycles), show topological ordering
- Nodes arranged in linear order
- All edges point in same direction
- Invalid if cycle exists

### Visual Elements

- Arrow indicators on edges
- Degree badges (in/out)
- Cycle highlight in red
- Topological order display
- DAG validation indicator

---

## Color Palette

| Element | Color | Hex Code |
|---------|-------|----------|
| Background | Deep Space Blue | #0a0a1a |
| Unvisited Node | Gray | #7f8c8d |
| Visiting Node | Yellow | #f1c40f |
| Visited Node | Green | #2ecc71 |
| Current Node | Bright Cyan | #00d4ff |
| Unvisited Edge | Dim Gray | #4a4a5a |
| Traversed Edge | Electric Blue | #3498db |
| BFS Wave | Ocean Blue | #1abc9c |
| DFS Beam | Purple | #9b59b6 |
| Shortest Path | Gold | #f39c12 |
| Cycle Edge | Red | #e74c3c |
| Component 1 | Coral | #ff6b6b |
| Component 2 | Teal | #4ecdc4 |
| Component 3 | Lavender | #a29bfe |

---

## Animation Timing

- Node state change: 200ms
- Edge traversal: 300ms
- BFS wave expansion: 500ms per level
- DFS step: 400ms
- Backtrack animation: 300ms
- Path highlight: 600ms
- Component coloring: 400ms per component
- Queue/Stack update: 200ms
- Camera transitions: 600ms ease-in-out
- Cycle detection highlight: 800ms
