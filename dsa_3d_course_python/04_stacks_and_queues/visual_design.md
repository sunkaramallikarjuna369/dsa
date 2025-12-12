# Visual Design: Stacks and Queues

## Environment Overview

The Stacks and Queues world is split into two distinct zones: a vertical tower area for stacks and a horizontal lobby area for queues. This spatial separation reinforces the different access patterns of these data structures.

### Background and Atmosphere

The environment is a futuristic facility with clean, minimalist architecture. The stack zone features a tall cylindrical chamber with a dark background and vertical light strips. The queue zone is a wide lobby with a glowing floor path and an elevator at one end. Both zones share a cohesive cyberpunk aesthetic with neon accents.

### Lighting

The stack zone uses dramatic top-down lighting that illuminates the plate tower from above, creating a spotlight effect on the top element. The queue zone has ambient floor lighting that traces the queue path, with brighter illumination at the front (elevator) and back (entry point).

### Camera Behavior

The camera can orbit 360 degrees around either zone. In the stack zone, the camera can rise and fall with the stack height, always keeping the top visible. In the queue zone, the camera can pan along the queue length. A split-screen mode shows both structures simultaneously for comparison.

### Interaction Ideas

Hovering over any element displays its value. Clicking the top of the stack triggers a pop animation. Clicking an "Add" button triggers push/enqueue with a value input. Speed controls adjust animation pace. A "Compare" mode runs identical operations on both structures to highlight ordering differences.

---

## Sub-Concept 1: Stack Operations (LIFO)

### 3D Metaphor

The stack is visualized as a tower of glowing translucent plates. Each plate is a flat disc (40cm diameter, 5cm thick) with the element value displayed on its top surface. Plates glow with a soft cyan color (#4ecdc4) and have a glass-like transparency.

**Push Operation**:
1. A new plate materializes above the tower with a bright flash
2. The plate descends smoothly onto the top of the stack
3. A subtle "clink" sound effect plays as it lands
4. The stack height increases visibly

**Pop Operation**:
1. The top plate highlights brighter
2. The plate lifts off the stack
3. The value is displayed prominently as it rises
4. The plate dissolves into particles
5. The stack height decreases

**Peek Operation**:
1. The top plate glows brighter momentarily
2. The value is displayed in a floating label
3. The plate remains in place (no removal)

**Stack Overflow/Underflow**:
- Overflow: Red warning flash, "Stack Full" message
- Underflow: Red warning flash, "Stack Empty" message

### Visual Elements

- Translucent glowing plates with value labels
- Vertical guide rails showing stack boundaries
- Height indicator on the side
- Top pointer arrow indicating current top
- Particle effects for push/pop animations

---

## Sub-Concept 2: Queue Operations (FIFO)

### 3D Metaphor

The queue is visualized as a line of glowing humanoid figures waiting in a lobby. Each figure is a simple stylized person shape (like a game piece) that glows with a unique color based on its value. The queue path is marked by a glowing line on the floor leading to an elevator door.

**Enqueue Operation**:
1. A new figure materializes at the entry point (back of queue)
2. The figure walks forward to join the back of the line
3. A "welcome" chime plays
4. The queue length increases

**Dequeue Operation**:
1. The front figure highlights
2. The elevator doors open with a sliding animation
3. The figure walks into the elevator
4. The elevator doors close
5. All remaining figures step forward one position
6. The queue length decreases

**Front Operation**:
1. The front figure glows brighter
2. Its value is displayed in a floating label
3. The figure remains in place

**Queue Full/Empty**:
- Full: "Lobby Full" sign illuminates
- Empty: "No One Waiting" message displays

### Visual Elements

- Stylized humanoid figures with value labels
- Glowing floor path marking queue positions
- Elevator doors at the front
- Entry portal at the back
- Queue length counter display
- Position markers on the floor

---

## Sub-Concept 3: Call Stack Visualization

### 3D Metaphor

The call stack during function execution is shown as a specialized stack where each plate represents a function call frame. Each plate is larger and contains more information: function name, parameters, local variables, and return address.

**Function Call**:
1. New frame plate materializes with function name prominently displayed
2. Parameters appear as smaller labels on the plate
3. The plate descends onto the call stack
4. An arrow shows the current execution point

**Function Return**:
1. The top frame highlights
2. Return value is extracted and displayed
3. The frame lifts off and dissolves
4. Execution returns to the frame below

**Recursive Calls**:
- Multiple frames with the same function name stack up
- Each frame shows different parameter values
- The depth of recursion is visually obvious

### Visual Elements

- Larger plates with function information
- Parameter and variable displays
- Return value extraction animation
- Execution pointer arrow
- Recursion depth indicator
- Stack overflow warning zone

---

## Sub-Concept 4: Expression Evaluation with Stack

### 3D Metaphor

Evaluating postfix expressions using a stack is shown with the plate tower alongside a conveyor belt of operators and operands.

**Setup**:
- Expression tokens appear on a conveyor belt approaching the stack
- Operands are shown as number cubes
- Operators are shown as symbol plates (+, -, *, /)

**Operand Processing**:
1. Number cube reaches the stack
2. It transforms into a plate and pushes onto the stack

**Operator Processing**:
1. Operator symbol reaches the stack
2. Top two plates pop off
3. The operator applies to them (visual calculation)
4. Result plate pushes onto the stack

**Final Result**:
- Last remaining plate shows the final answer
- Celebration effect with the result

### Visual Elements

- Conveyor belt with expression tokens
- Number cubes transforming to plates
- Operator symbols with visual effects
- Calculation animations
- Result highlight

---

## Sub-Concept 5: BFS Queue Visualization

### 3D Metaphor

Breadth-first search using a queue is shown with a graph structure alongside the queue lobby. Nodes from the graph join the queue as they're discovered.

**Setup**:
- Graph nodes float in space, connected by edges
- Queue lobby is positioned below the graph
- Visited nodes change color

**BFS Process**:
1. Start node highlights and joins the queue (enqueue)
2. Front node is processed (dequeue)
3. Its unvisited neighbors join the queue
4. Process repeats until queue is empty

**Level Visualization**:
- Nodes discovered at the same level have the same color
- The wavefront of discovery is visible
- Queue shows the frontier of exploration

### Visual Elements

- Graph with floating nodes and edges
- Queue lobby below the graph
- Color-coded discovery levels
- Visited/unvisited node states
- Edge highlighting during neighbor discovery

---

## Color Palette

| Element | Color | Hex Code |
|---------|-------|----------|
| Background | Dark Blue-Gray | #1a1a2e |
| Stack plates | Soft Cyan | #4ecdc4 |
| Queue figures | Warm Orange | #f39c12 |
| Active/highlighted | Bright White | #ffffff |
| Push/enqueue | Success Green | #2ecc71 |
| Pop/dequeue | Action Blue | #3498db |
| Error/warning | Alert Red | #e74c3c |
| Elevator doors | Metallic Silver | #bdc3c7 |
| Floor path | Neon Purple | #9b59b6 |
| Call stack frames | Golden Yellow | #f1c40f |

---

## Animation Timing

- Push plate descent: 400ms ease-out
- Pop plate ascent: 300ms ease-in
- Plate dissolve: 500ms fade
- Enqueue figure walk: 600ms
- Dequeue elevator sequence: 800ms total
- Queue shift forward: 400ms per position
- Function call frame: 500ms
- Expression token movement: 300ms per token
- BFS node discovery: 400ms per node
- Camera transitions: 600ms ease-in-out
