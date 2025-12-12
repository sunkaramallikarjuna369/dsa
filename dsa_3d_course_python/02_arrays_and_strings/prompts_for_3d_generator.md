# 3D Generator Prompts: Arrays and Strings

These prompts are designed for use with 3D generation tools such as Three.js, WebGL, Blender scripting agents, or AI-powered 3D scene generators. Each prompt provides sufficient detail to create an educational, interactive 360-degree visualization.

---

## Prompt 1: Array Index Access Corridor

Generate a 360-degree, interactive 3D scene of a futuristic circular corridor representing an array data structure. The corridor curves gently in a wide arc, with the floor divided into 20 perfectly aligned square tiles numbered 0 through 19. Each tile is a metallic platform with its index number embossed in glowing cyan digits (#00d4ff).

Above each tile floats a translucent cube (30cm side) containing a holographic integer value. The cubes hover 50cm above their tiles and rotate slowly. The corridor walls are dark slate (#1a1a2e) with subtle blue circuit patterns that pulse gently.

The camera can orbit 360 degrees around the corridor's central axis and zoom to examine individual tiles. When the user clicks on any tile, a vertical beam of bright cyan light instantly connects the ceiling to that tile, illuminating both the tile and its floating cube. A floating label appears showing "O(1) Access" with a timer displaying "1 operation".

Include a formula overlay that appears during access: "base_address + (index × 4 bytes) = target_address" with each component highlighting sequentially. Add an input field where users can type an index (0-19) and press Enter to trigger the access animation for that position.

The scene should have ambient lighting from above and tile-based uplighting. All labels must be readable from any camera angle using billboard text rendering.

---

## Prompt 2: Array Iteration Wave

Generate a 360-degree, interactive 3D scene showing array iteration as a sweeping wave of light through a corridor of 15 numbered tiles. The corridor is straight, extending into the distance with tiles numbered 0-14. Each tile has a floating cube above it containing a random integer value.

**Forward Iteration**: When activated, a bright cyan wavefront (#00d4ff) travels from tile 0 toward tile 14, illuminating each tile sequentially. The wave leaves a fading trail (opacity decreasing over 2 seconds) showing visited elements. A counter in the top-right displays "Elements Visited: X/15" incrementing with each tile.

**Reverse Iteration**: A purple wave (#9b59b6) travels from tile 14 toward tile 0, with the same trailing effect but distinct color.

**Two-Pointer Technique**: Two beams start simultaneously - a cyan beam at tile 0 and a magenta beam (#e91e63) at tile 14. They move toward each other at the same speed. Floating markers above each beam show "left" and "right" labels. When the beams meet at the center, a flash effect occurs and text displays "Pointers Crossed".

Include play/pause controls, speed adjustment (0.5x, 1x, 2x), and buttons to select iteration type. The camera can orbit around the corridor and follow the wave movement. Add a code snippet panel showing the corresponding Python loop syntax that highlights the current line being executed.

---

## Prompt 3: Sliding Window Visualization

Generate a 360-degree, interactive 3D scene demonstrating the sliding window technique on an array corridor. The corridor contains 12 tiles (indices 0-11) with floating cubes showing integer values: [2, 1, 5, 1, 3, 2, 8, 1, 3, 2, 4, 5].

A glowing rectangular frame (the "window") encompasses exactly 4 consecutive tiles. The frame has a golden-yellow color (#ffd700) with distinct left edge (green, #2ecc71) and right edge (blue, #3498db). Elements within the window are elevated 20cm higher than others and connected by thin glowing threads.

**Animation Sequence**:
1. Window starts at position [0-3], highlighting tiles 0, 1, 2, 3
2. A floating display shows "Window Sum: 9" (2+1+5+1)
3. Window slides right by one position to [1-4]
4. The element leaving (tile 0, value 2) dims and lowers
5. The element entering (tile 4, value 3) brightens and elevates
6. Display updates to "Window Sum: 10" (1+5+1+3)
7. Continue sliding until window reaches [8-11]

Include a "Maximum Sum Found" indicator that highlights when the current window sum exceeds all previous sums. Add controls for window size (adjustable 2-6), manual step-through, and auto-play. The camera should smoothly follow the window as it slides, maintaining a view that shows both the window and upcoming elements.

---

## Prompt 4: Two-Pointer Array Reversal

Generate a 360-degree, interactive 3D scene showing the two-pointer technique for reversing an array in place. The corridor contains 8 tiles with floating letter cubes spelling "ALGORITHM" (indices 0-7 showing A, L, G, O, R, I, T, H... wait, that's 9 letters, use "HELLO" for 5 tiles or "REVERSE" for 7 tiles).

Use 7 tiles spelling "REVERSE" (R, E, V, E, R, S, E).

Two pointer beams are positioned:
- Left pointer (cyan, #00bcd4) starts at tile 0
- Right pointer (magenta, #e91e63) starts at tile 6

**Swap Animation Sequence**:
1. Both pointers highlight their tiles
2. The cubes at positions 0 and 6 lift up simultaneously
3. The cubes cross paths in an arc (the R and E swap)
4. Cubes descend to their new positions
5. Pointers move inward (left to 1, right to 5)
6. Repeat swap for positions 1 and 5
7. Continue until pointers meet at center

After completion, the array reads "ESREVER" (REVERSE reversed). Include a step counter, swap counter, and a panel showing the array state after each swap. The camera can orbit freely but auto-focuses on the active swap region. Add a "Reset" button to restart the animation.

---

## Prompt 5: String Concatenation and Immutability

Generate a 360-degree, interactive 3D scene demonstrating string immutability and concatenation in Python. The scene contains two parallel string corridors floating in a dark space with subtle grid lines.

**Corridor A**: 5 tiles spelling "HELLO" with character cubes (white text on translucent cubes)
**Corridor B**: 5 tiles spelling "WORLD" positioned 3 meters to the right of Corridor A

**Concatenation Animation**:
1. Both corridors are labeled with floating text: `str_a = "HELLO"` and `str_b = "WORLD"`
2. When concatenation is triggered, a bright flash occurs
3. A NEW corridor materializes below the original two, with 10 tiles
4. Characters from both original corridors duplicate (not move) into the new corridor
5. The new corridor displays "HELLOWORLD" and is labeled `str_c = str_a + str_b`
6. A prominent label appears: "New String Object Created - Originals Unchanged"
7. The original corridors remain intact, demonstrating immutability

Include a memory address display showing different addresses for each string object. Add buttons to demonstrate other operations:
- **Slicing**: Highlight a range in a string, show it duplicating into a new mini-corridor
- **Upper/Lower**: Show character cubes transforming (with flash effect) into a new corridor

The camera can orbit around all corridors. Use color coding: original strings in cyan, new strings in purple (#9b59b6), to emphasize that new objects are created.

---

## Prompt 6: Array Insert and Delete Operations

Generate a 360-degree, interactive 3D scene showing the cost of inserting and deleting elements in the middle of an array. The corridor contains 8 tiles (indices 0-7) with floating number cubes: [10, 20, 30, 40, 50, 60, 70, 80].

**Insert Operation** (insert 35 at index 3):
1. A new cube labeled "35" appears above the corridor, glowing green
2. All cubes from index 3 onward (40, 50, 60, 70, 80) lift up
3. These cubes shift right by one position in a cascading wave
4. A new tile materializes at position 3
5. The "35" cube descends into position 3
6. Operation counter shows "5 elements shifted - O(n) operation"

**Delete Operation** (delete element at index 2):
1. The cube at index 2 (value 30) highlights red
2. The cube lifts up and fades away (deletion effect)
3. All cubes from index 3 onward shift left by one position
4. The rightmost tile fades out as the array shrinks
5. Operation counter shows "5 elements shifted - O(n) operation"

Include side-by-side comparison with append operation (O(1)) showing a cube simply appearing at the end without any shifting. Add a complexity comparison panel showing:
- Access: O(1)
- Append: O(1) amortized
- Insert at index: O(n)
- Delete at index: O(n)

The camera should follow the shifting elements during operations. Include step-by-step controls and a reset button.

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
