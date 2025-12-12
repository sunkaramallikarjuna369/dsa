# 3D Generator Prompts: Time Complexity and Recursion

These prompts are designed for use with 3D generation tools such as Three.js, WebGL, Blender scripting agents, or AI-powered 3D scene generators. Each prompt provides sufficient detail to create an educational, interactive 360-degree visualization.

---

## Prompt 1: Complexity Classes Observatory

Generate a 360-degree, interactive 3D scene of a cosmic observatory floating in deep space. The observatory is a circular platform with five distinct chambers arranged in a semicircle, each representing a different time complexity class. The background is a dark indigo gradient (#0a0a1a) with distant stars and slowly drifting particle effects simulating cosmic dust.

At the center of the platform stands a large holographic clock with translucent cyan hands. The clock's speed varies based on which chamber is active. The camera can orbit fully around the observatory and zoom in on individual chambers.

**Chamber 1 - O(1) Constant**: A small cube-shaped room with stable blue walls (#4a9eff). Inside floats a single glowing orb. Outside the transparent walls, input elements (small white spheres) appear, but the orb remains unchanged regardless of count. Label this chamber "O(1) - Constant Time" with floating holographic text.

**Chamber 2 - O(log n) Logarithmic**: A spiral staircase descending through floating hexagonal platforms. Each platform is half the width of the one above. The structure glows serene green (#2ecc71). Particles flow downward along the spiral. Label: "O(log n) - Logarithmic Time".

**Chamber 3 - O(n) Linear**: A long straight corridor with evenly spaced pillars of white-blue light (#5dade2). As the input slider increases, new pillars materialize at the far end, extending the corridor proportionally. Label: "O(n) - Linear Time".

**Chamber 4 - O(n log n) Linearithmic**: A circular arena with concentric rings. Each ring contains n glowing nodes that pulse in waves rippling outward. The rings are colored in shifting cyan and teal gradients. Label: "O(n log n) - Linearithmic Time".

**Chamber 5 - O(n²) Quadratic**: A vast square arena where elements form a 2D grid on the floor. As n increases, the grid expands quadratically. Floor tiles light up in expanding squares, transitioning from yellow (#f1c40f) at center to deep orange (#f39c12) at edges. Label: "O(n²) - Quadratic Time".

Include an interactive slider labeled "Input Size (n)" that adjusts from 1 to 100. As n changes, all chambers update simultaneously to show their respective growth. The holographic clock hands spin faster for higher complexity classes. Add tooltips on hover explaining each complexity class.

---

## Prompt 2: Recursion Mirror Tower

Generate a 360-degree, interactive 3D scene of a vertical tower composed of stacked hexagonal mirror chambers, representing recursive function calls. The environment background is deep space with purple nebula accents. The camera can orbit around the tower and zoom to follow the recursion descent.

The tower consists of 8 hexagonal chambers stacked vertically. Each chamber has reflective walls with a subtle magenta tint (#9b59b6). The topmost chamber is the largest, and each subsequent chamber below is 15% smaller, representing the recursive breakdown of the problem.

**Initial State**: The top chamber contains a floating holographic display showing the function call with its parameters (e.g., "factorial(5)"). A glowing portal on the floor connects to the chamber below.

**Recursion Descent Animation**: When activated, a glowing avatar representing the current execution steps through the portal into the smaller chamber below. The new chamber displays the recursive call (e.g., "factorial(4)"). This continues until reaching the base case chamber at the bottom, which has a solid golden floor (#f1c40f) instead of a portal, labeled "Base Case".

**Return Phase Animation**: Once the base case is reached, a golden orb representing the return value (e.g., "1") floats upward through the portals. At each chamber, the orb combines with the local computation (visualized as multiplication symbols and numbers merging), growing brighter and displaying the accumulated result until it reaches the top chamber with the final answer.

**Call Stack Sidebar**: On the right side of the scene, display a vertical bar chart showing the call stack. Each bar is labeled with the function call and parameters. Bars stack upward during descent and dissolve from top down during returns, with particles carrying return values.

Include play/pause controls and a speed slider. Add a "Stack Overflow Warning" indicator that flashes red (#e74c3c) if recursion depth exceeds a safe threshold. Hovering over any chamber shows a tooltip with the current state of that recursive call.

---

## Prompt 3: Iterative vs Recursive Comparison

Generate a 360-degree, interactive 3D scene showing a split environment comparing iterative and recursive approaches to solving the same problem (factorial calculation). The camera can orbit around both structures and zoom into either side.

**Left Side - Iterative Conveyor System**: An industrial-themed horizontal conveyor belt system. Elements (numbered cubes from 1 to n) enter from the left on a glowing blue conveyor belt. A mechanical robotic arm picks up each cube and brings it to a central processing station where it multiplies with an accumulator display. The result updates on a large digital counter. Gears and pistons are visible, emphasizing the mechanical, step-by-step nature. The loop counter displays prominently, incrementing with each cycle. Color scheme: metallic silver and industrial blue (#3498db).

**Right Side - Recursive Mirror Tower**: The hexagonal mirror tower from Prompt 2, scaled to fit beside the conveyor system. Same magenta-tinted chambers (#9b59b6) with descending sizes and golden base case floor.

**Synchronized Execution**: Both systems process the same input (e.g., n=5) simultaneously. The conveyor processes elements 1, 2, 3, 4, 5 sequentially while the tower descends through factorial(5), factorial(4), etc. Timing is synchronized so equivalent computational steps occur at the same moment.

**Memory Usage Visualization**: Between the two systems, display two vertical memory meters. The iterative meter shows constant low memory usage (a short bar). The recursive meter grows taller with each recursive call, showing stack frame accumulation. Label these "Iterative Memory" and "Recursive Memory".

**Result Convergence**: At the bottom center, a platform displays the final result. Glowing paths from both systems converge here, showing that both approaches produce the same answer (120 for factorial(5)).

Include controls to change the input value n (1-10), play/pause, and speed adjustment. Add floating labels explaining key differences: "Single context" for iterative, "Nested contexts" for recursive. The 360-degree orbit allows viewing the comparison from any angle.

---

## Prompt 4: Growth Rate Visualization Graph

Generate a 360-degree, interactive 3D scene displaying animated growth curves for different time complexities as 3D ribbons floating in space. The background is a dark grid (#1a1a2e) with subtle blue grid lines extending to the horizon, creating a futuristic data visualization environment.

**3D Graph Space**: Create a three-dimensional coordinate system with the X-axis representing input size n (0 to 100), the Y-axis representing operations count (0 to 10000), and the Z-axis providing depth for separating different curves. Axis labels float beside each axis with clear numerical markers.

**Growth Curves as 3D Ribbons**: Each complexity class is represented as a glowing ribbon that traces its growth curve through the 3D space:

- **O(1)**: A flat horizontal ribbon at y=1, colored calm blue (#4a9eff), barely rising regardless of x.
- **O(log n)**: A gently curving ribbon that rises slowly, colored serene green (#2ecc71).
- **O(n)**: A straight diagonal ribbon rising linearly, colored neutral cyan (#5dade2).
- **O(n log n)**: A ribbon curving slightly above linear, colored teal (#1abc9c).
- **O(n²)**: A ribbon that curves sharply upward, colored warning orange (#f39c12).
- **O(2^n)**: A ribbon that shoots nearly vertical after small n values, colored alert red (#e74c3c), demonstrating exponential explosion.

**Animation**: As the user drags a slider for n, a vertical plane sweeps along the X-axis, and each ribbon illuminates at the intersection point, showing the current operation count for that complexity at that input size. Numerical values display at each intersection.

**Interactive Features**: Clicking on any ribbon highlights it and displays its Big O formula and a brief explanation. The camera can orbit 360 degrees around the graph, allowing users to view the dramatic differences from various angles. A "Compare" mode allows selecting two complexities to highlight while dimming others.

Include a legend in the corner mapping colors to complexity classes. Add subtle particle effects along each ribbon to emphasize data flow.

---

## Prompt 5: Recursive Tree Visualization (Fibonacci)

Generate a 360-degree, interactive 3D scene showing the recursive call tree for computing Fibonacci numbers. The environment is a dark forest clearing at night with bioluminescent elements, creating an organic feel for the tree structure.

**Recursive Call Tree**: A 3D tree structure where each node is a glowing sphere representing a function call. The root node at the top displays "fib(6)" and branches downward. Each node branches into two children (fib(n-1) and fib(n-2)) until reaching base cases fib(1) and fib(0).

**Node Design**: Each node is a translucent sphere with the function call displayed inside (e.g., "fib(4)"). Nodes are colored based on their depth: root is bright cyan (#5dade2), and colors shift through green (#2ecc71) to yellow (#f1c40f) as depth increases. Base case nodes (fib(0) and fib(1)) are solid gold (#f1c40f) and smaller than other nodes.

**Edges**: Connections between nodes are glowing vines or branches that pulse with light when data flows through them. Left branches (n-1 calls) are tinted blue, right branches (n-2 calls) are tinted green.

**Overlapping Subproblems Highlight**: Nodes computing the same value (e.g., multiple fib(2) calls) pulse in synchronization and are connected by faint dotted lines across the tree, visually demonstrating redundant computation. A counter shows "Redundant Calls: X" updating as the tree builds.

**Animation Sequence**: 
1. Tree builds top-down, with nodes appearing and edges growing as recursive calls are made.
2. Once base cases are reached, return values (small numbered orbs) float upward through the edges.
3. At each node, child values combine (addition visualized as orbs merging) to produce the parent's return value.
4. Final answer glows brightly at the root.

**Camera**: Full 360-degree orbit around the tree. Zoom to inspect individual nodes. A "flatten" view option shows the tree from directly above, revealing the binary structure.

Include a slider to change the input (fib(3) to fib(8)) and observe how the tree grows. Add a comparison panel showing how memoization would prune redundant branches (grayed-out nodes that would be skipped).

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
