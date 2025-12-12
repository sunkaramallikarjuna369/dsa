# 3D Generator Prompts: Graphs and Traversals

These prompts are designed for use with 3D generation tools such as Three.js, WebGL, Blender scripting agents, or AI-powered 3D scene generators. Each prompt provides sufficient detail to create an educational, interactive 360-degree visualization.

---

## Prompt 1: Graph Structure Visualization

Generate a 360-degree, interactive 3D scene showing a graph as floating nodes connected by edges in space. The background is deep space blue (#0a0a1a) with subtle nebula effects.

**Graph Structure** (6 nodes, 7 edges):
- Nodes: A, B, C, D, E, F
- Edges: A-B, A-C, B-D, B-E, C-E, C-F, E-F

**Node Visualization**:
- Each node is a glowing sphere (20cm diameter)
- Node labels displayed on sphere surface (white text)
- Nodes positioned in 3D space with good separation
- Unvisited state: gray (#7f8c8d)
- Small badge showing degree (number of connections)

**Edge Visualization**:
- Glowing beams connecting nodes
- Beam color: dim gray (#4a4a5a) for untraversed
- Beam thickness: 2cm
- Subtle pulse animation along edges

**Dual Representation View**:
- Toggle button to switch between:
  1. Spatial view (nodes floating in 3D)
  2. Adjacency list view (nodes with neighbor lists)
  3. Adjacency matrix view (6x6 grid)
- Smooth transition animation between views

**Interactive Elements**:
- Click node to highlight it and its neighbors
- Hover shows node info (label, degree, neighbors)
- Drag to rotate entire graph
- Zoom in/out capability

The camera can orbit 360 degrees around the graph structure, with preset views for front, top, and isometric angles.

---

## Prompt 2: Breadth-First Search (BFS) Visualization

Generate a 360-degree, interactive 3D scene demonstrating BFS traversal on a graph. Start from node A and explore all reachable nodes level by level.

**Graph Setup**:
- 8 nodes arranged in 3D space
- Nodes: 1 (source), 2, 3, 4, 5, 6, 7, 8
- Edges: 1-2, 1-3, 2-4, 2-5, 3-6, 3-7, 5-8, 6-8

**BFS Animation Sequence**:

Level 0: "Start at source node 1"
- Node 1 pulses bright cyan (#00d4ff)
- "Distance: 0" label appears
- First wave ring emanates from node 1

Level 1: "Explore neighbors of node 1"
- Wave expands to nodes 2 and 3
- Nodes 2, 3 turn yellow (#f1c40f) then green (#2ecc71)
- Edges 1-2, 1-3 glow blue (#3498db)
- "Distance: 1" labels appear

Level 2: "Explore neighbors of nodes 2 and 3"
- Wave expands to nodes 4, 5, 6, 7
- These nodes transition yellow to green
- Corresponding edges glow
- "Distance: 2" labels appear

Level 3: "Explore remaining nodes"
- Wave reaches node 8 from both 5 and 6
- Node 8 turns green
- "Distance: 3" label appears

**Queue Visualization**:
- Horizontal queue bar at bottom of scene
- Nodes enter queue from right, exit from left
- Current processing node highlighted
- Queue updates in sync with traversal

**Visual Elements**:
- Concentric distance rings around source
- Parent pointer arrows (dim, showing path back)
- Level numbers on rings
- Traversal order counter

Controls: Play, Pause, Step Forward, Speed Slider, Reset

---

## Prompt 3: Depth-First Search (DFS) Visualization

Generate a 360-degree, interactive 3D scene demonstrating DFS traversal on a graph. Show the exploration beam diving deep before backtracking.

**Graph Setup**:
- Same 8-node graph as BFS prompt
- Nodes: 1 (source), 2, 3, 4, 5, 6, 7, 8

**DFS Animation Sequence**:

Step 1: "Start DFS from node 1"
- Node 1 glows purple (#9b59b6)
- Exploration beam initializes
- Stack shows: [1]

Step 2: "Explore first neighbor (node 2)"
- Beam travels from 1 to 2
- Node 2 turns purple
- Edge 1-2 glows
- Stack shows: [1, 2]

Step 3: "Go deeper to node 4"
- Beam continues to node 4
- Node 4 turns purple
- Stack shows: [1, 2, 4]

Step 4: "Node 4 has no unvisited neighbors - backtrack"
- Node 4 turns green (finished)
- Beam retraces to node 2
- Backtrack animation (beam dims and returns)
- Stack shows: [1, 2]

Step 5: "Explore node 5 from node 2"
- Beam goes to node 5
- Stack shows: [1, 2, 5]

Step 6: "Continue to node 8"
- Beam goes to node 8
- Stack shows: [1, 2, 5, 8]

(Continue until all nodes visited)

**Stack Visualization**:
- Vertical stack on side of scene
- Push animation when going deeper
- Pop animation when backtracking
- Current top of stack highlighted

**Discovery/Finish Times**:
- Discovery time badge appears when node first visited
- Finish time badge appears when backtracking complete
- Format: "d:X/f:Y" where X is discovery, Y is finish time

**Trail Visualization**:
- Glowing trail shows current path
- Completed paths dim but remain visible
- Backtracked edges shown in different color

---

## Prompt 4: Connected Components Visualization

Generate a 360-degree, interactive 3D scene showing a disconnected graph with multiple connected components, each colored differently.

**Graph Setup** (3 components):
- Component 1 (Red): Nodes A, B, C with edges A-B, B-C, A-C
- Component 2 (Teal): Nodes D, E, F, G with edges D-E, E-F, F-G, D-G
- Component 3 (Lavender): Nodes H, I with edge H-I

**Initial State**:
- All nodes gray (#7f8c8d)
- All edges dim
- "Components: ?" displayed

**Discovery Animation**:

Phase 1: "Discover Component 1"
- BFS/DFS from node A
- Nodes A, B, C turn coral (#ff6b6b)
- Edges within component glow coral
- "Component 1: 3 nodes" label

Phase 2: "Discover Component 2"
- Start from unvisited node D
- Nodes D, E, F, G turn teal (#4ecdc4)
- Edges glow teal
- "Component 2: 4 nodes" label

Phase 3: "Discover Component 3"
- Start from unvisited node H
- Nodes H, I turn lavender (#a29bfe)
- Edge glows lavender
- "Component 3: 2 nodes" label

**Final Display**:
- "Total Components: 3"
- Component sizes: 3, 4, 2
- Largest component highlighted
- Connectivity percentage shown

**Interactive Features**:
- Click component to isolate view
- Toggle to show/hide individual components
- Component statistics panel

---

## Prompt 5: Shortest Path Visualization (Unweighted)

Generate a 360-degree, interactive 3D scene showing BFS finding the shortest path between two nodes in an unweighted graph.

**Graph Setup**:
- 10 nodes in a complex arrangement
- Multiple paths between source and target
- Source: Node S (green glow)
- Target: Node T (red glow)

**Path Finding Animation**:

Step 1: "Initialize BFS from source S"
- Source S pulses green
- BFS waves begin expanding

Step 2-4: "Waves expand level by level"
- Each level shown as expanding ring
- Nodes colored by distance from source
- Parent pointers recorded (dim arrows)

Step 5: "Wave reaches target T"
- Target T discovered
- "Shortest path found!" message
- Path length displayed

Step 6: "Trace back shortest path"
- Follow parent pointers from T to S
- Path edges turn gold (#f39c12)
- Path nodes pulse with success effect
- Alternative (longer) paths shown dimly

**Path Comparison**:
- Shortest path: highlighted in gold
- Alternative paths: shown in gray
- Path lengths compared
- "Optimal path: X edges" display

**Interactive Elements**:
- Click any two nodes to find shortest path
- Show all paths option
- Distance from source for all nodes

---

## Prompt 6: Directed Graph and Cycle Detection

Generate a 360-degree, interactive 3D scene showing a directed graph with cycle detection using DFS.

**Graph Setup** (Directed, with cycle):
- Nodes: 1, 2, 3, 4, 5
- Directed edges: 1→2, 2→3, 3→4, 4→2 (creates cycle), 1→5

**Directed Edge Visualization**:
- Edges have arrow heads showing direction
- Arrow glows when traversed in valid direction
- Attempting reverse traversal blocked (X indicator)
- In-degree and out-degree badges on nodes

**Cycle Detection Animation**:

Step 1: "Start DFS from node 1"
- Node 1 marked as "in progress" (yellow)
- DFS begins

Step 2: "Explore path 1→2→3→4"
- Each node marked "in progress"
- Path shown as connected yellow nodes

Step 3: "From node 4, edge to node 2 detected"
- Edge 4→2 highlighted
- Node 2 is already "in progress" (ancestor)
- "BACK EDGE DETECTED!" alert

Step 4: "Cycle found!"
- Cycle path highlighted in red (#e74c3c)
- Cycle: 2→3→4→2
- "Graph contains cycle" message
- Cycle nodes pulse red

**Topological Sort (for DAG)**:
- If no cycle, show topological ordering
- Nodes arranged in linear order
- All edges point left to right
- "Valid topological order" message

**Node States**:
- White: Unvisited
- Yellow: In progress (on current path)
- Green: Completed (all descendants visited)
- Red: Part of cycle

---

## Prompt 7: Graph Representations Comparison

Generate a 360-degree, interactive 3D scene comparing adjacency list and adjacency matrix representations of the same graph.

**Graph**:
- 5 nodes: A, B, C, D, E
- Edges: A-B, A-C, B-C, B-D, C-E

**Split View**:

**Left Side - Adjacency List**:
- Each node displayed with its neighbor list
- Format: "A: [B, C]", "B: [A, C, D]", etc.
- Lists float beside their source nodes
- Clicking a neighbor highlights the edge

**Right Side - Adjacency Matrix**:
- 5x5 grid floating in space
- Row and column headers: A, B, C, D, E
- Cell [i][j] = 1 if edge exists, 0 otherwise
- Cells glow when edge exists
- Clicking cell highlights corresponding edge

**Center - Actual Graph**:
- Visual graph representation
- Edges highlighted when corresponding list item or matrix cell selected

**Comparison Panel**:
- Space complexity: List O(V+E) vs Matrix O(V²)
- Edge lookup: List O(degree) vs Matrix O(1)
- Add edge: List O(1) vs Matrix O(1)
- Best use cases for each

**Interactive Features**:
- Add/remove edges and see both representations update
- Highlight edge in one view, see it in others
- Toggle between sparse and dense graph examples

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
